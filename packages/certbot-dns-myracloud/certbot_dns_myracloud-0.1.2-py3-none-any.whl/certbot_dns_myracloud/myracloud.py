import logging
from typing import Callable, Dict, Union
import hmac, hashlib, base64, datetime
import requests, json
from certbot import errors
from certbot.plugins import dns_common

logger = logging.getLogger(__name__)

class _MyracloudClient(object):
    """
    A client to interact with the Myracloud DNS API.

    Attributes:
        auth_token (str): The authentication token for the API.
        auth_secret (str): The authentication secret for the API.
    """

    def __init__(self, auth_token: str, auth_secret: str):
        """
        Initialize the MyracloudClient.

        :param auth_token: The authentication token for the API.
        :param auth_secret: The authentication secret for the API.
        """
        self.auth_token = auth_token
        self.auth_secret = auth_secret

        # constants
        self.myraApiScheme       = 'https'
        self.myraApiHost         = 'api.myracloud.com'
        self.api_method_create   = 'PUT'
        self.api_method_retrieve = 'GET'
        self.api_method_update   = 'POST'
        self.api_method_delete   = 'DELETE'

    def _auth_sign(self, requestDate:str, requestMethod:str, requestUri:str, requestBody:str, requestContentType:str='application/json'):
        """
        generate authorization token
        :param requestDate: the datetime of the request, in the form %Y-%m-%dT%H:%M:%S%z, where %z is for example "02:00" instead of "0200"
        :param requestMethod: the method to use (PUT,GET,POST,DELETE)
        :param requestUri: the api endpoint
        :param requestBody: the body to send (and sign over)
        :param requestContentType: content-type header to use
        """

        x = hashlib.md5()
        x.update(requestBody.encode())
        reqMD5 = x.hexdigest()

        _signing_string     = reqMD5 + '#' + requestMethod + '#' + requestUri + '#' + requestContentType + '#' + requestDate
        _datekey_hexmac     = hmac.new('MYRA{}'.format(self.auth_secret).encode(), digestmod=hashlib.sha256)
        _datekey_hexmac.update(requestDate.encode())
        _datekey_hexmac_s     = str(_datekey_hexmac.hexdigest())

        _signingkey_hexmac  = hmac.new(_datekey_hexmac_s.encode(), digestmod=hashlib.sha256)
        _signingkey_hexmac.update('myra-api-request'.encode())
        _signingkey_hexmac_s  = _signingkey_hexmac.hexdigest()

        _signature          = hmac.new(_signingkey_hexmac_s.encode(), digestmod=hashlib.sha512)
        _signature.update(_signing_string.encode())
        _signature_b          = _signature.digest()
        _signature_s          = base64.b64encode(_signature_b)

        _request_authorization = 'MYRA {}:{}'.format(self.auth_token, _signature_s.decode("utf-8"))
        return _request_authorization

    def _response_check(self, resp:requests.Response) -> None:
        """
        parses query response and displays it nicely.
        :param resp: the request.Response to check
        """
        if resp.status_code == 403:
            raise Exception('authentication failed')

        elif resp.status_code == 200:
            try:
                r = json.loads(resp.text)
            except Exception as e:
                raise Exception("error parsing response from server", resp.text)

            if r['error']:
                raise Exception(r['violationList'])
            else:
                if 'list' in r:
                    return r['list']
                elif 'targetObject' in r:
                    return r['targetObject']
                elif 'result' in r:
                    return r['result']
                else:
                    raise Exception('unknown return-value: ', r)
            return r

        else:
            raise Exception('unknown http-status from api: {}'.format(resp.status_code))

    def request(self, requestMethod:str, requestUri:str, requestBody: str = ''):
        """
        generic request handler for functions not yet covered in this module

        :param requestMethod: one of client.api_method_create, client.api_method_create, client.api_method_update, client.api_method_delete
        :param requestUri: the api endpoint
        :param requestBody: the body to send
        """
        url = '{}://{}{}'.format(self.myraApiScheme, self.myraApiHost, requestUri)

        if requestBody:
            requestBody = json.dumps(requestBody, separators=(',',':')).strip()

        # gen datestring to sign with
        d = datetime.datetime.now(datetime.timezone.utc).astimezone().strftime('%Y-%m-%dT%H:%M:%S%z')
        requestDate = '%s:%s' % (d[:-2], d[-2:])

        headers = {
            "Content-Type": "application/json",
            "Date": requestDate,
            "Authorization": self._auth_sign(requestDate, requestMethod, requestUri, requestBody)
        }

        if requestMethod == self.api_method_retrieve:
            resp = requests.get(url, headers=headers)

        elif requestMethod == self.api_method_create:
            resp = requests.put(url, data=requestBody, headers=headers)

        elif requestMethod == self.api_method_delete:
            resp = requests.delete(url, data=requestBody, headers=headers)

        elif requestMethod == self.api_method_update:
            resp = requests.post(url, data=requestBody, headers=headers)

        return self._response_check(resp)

    def dns_get(self, domain:str):
        """
        get all dns-records for a given domain

        :param domain: the myracloud domain for which to get dns-records
        """
        requestUri = '/en/rapi/dnsRecords/{}/1'.format(domain)
        return self.request(self.api_method_retrieve, requestUri)

    def dns_search(self, domain:str, value:str, recordType:str='A'):
        """
        search for specific recordTypes matching a certain value inside a given domain

        :param domain: the myracloud domain within which to search dns-records
        :param value: the value of the record
        :param recordType: the type of the record (A,AAAA, CNAME, TXT, MX, NS, SRV, CAA)
        """
        requestUri = '/en/rapi/dnsRecords/{}/1?search={}&recordTypes={}'.format(domain, value, recordType)
        return self.request(self.api_method_retrieve, requestUri)

    def dns_create(self, domain:str, fqdn:str, value:str, ttl:str="300", recordType:str='A', active:bool=True, enabled:bool=True):
        """
        create a DNS record for a given domain

        :param domain: the myracloud domain within which to create the dns-record
        :param fqdn: the full fqdn of the record to create
        :param value: the value of the record
        :param ttl: the TTL of the record (default: 300)
        :param recordType: the type of the record (A,AAAA, CNAME, TXT, MX, NS, SRV, CAA)
        :param active: if protection is enabled for the record
        :param enabled: if the record is currently being served by Myracloud DNS
        """
        requestUri = '/en/rapi/dnsRecords/{}'.format(domain)
        requestBody = {'name':fqdn, 'value':value, 'ttl':ttl, 'recordType':recordType, 'enabled':enabled, 'active':active}

        return self.request(self.api_method_create, requestUri, requestBody)

    def dns_delete(self, domain:str='', recordId:int=0, modified:int=0):
        """
        delete a DNS record from Myra DNS system given by recordId

        :param domain: the myracloud domain within which to create the dns-record
        :param recordId: the id of the record (gathered before from dns_search for example)
        :param modifed: the last modification datetime of the record to delete
        """
        if domain and recordId and modified:
            requestUri = '/en/rapi/dnsRecords/{}'.format(domain)
            requestBody = {'id':recordId, 'modified':modified}
            return self.request(self.api_method_delete, requestUri, requestBody)
        raise Exception('invalid params given for dns_delete')

    def add_txt_record(self, domain: str, validation_name: str, validation: str):
        """
        Add a TXT record using the supplied information.

        :param domain: The domain one level above the validation name.
        :param validation_name: The acme challenge record name.
        :param validation: The acme challenge record content.
        """
        self.dns_create(domain=domain, fqdn=validation_name, value=validation, recordType='TXT')

    def del_txt_record(self, domain: str, validation_name: str, validation: str):
        """
        Delete a TXT record using the supplied information.

        :param domain: The zone dnsName.
        :param validation_name: The record name.
        :param validation: The record content.
        """
        # get record id
        records = self.dns_search(domain=domain, value=validation, recordType='TXT')
        if records:
            id = 'id' in records[0] and records[0]['id'] or 0
            modified = 'modified' in records[0] and records[0]['modified'] or 0

            if id and modified:
                self.dns_delete(domain=domain, recordId=id, modified=modified)

class Authenticator(dns_common.DNSAuthenticator):
    """
    Myracloud DNS Authenticator.

    This authenticator resolves a DNS01 challenge by publishing the required
    validation token to a Myracloud DNS record.

    Attributes:
        credentials: A configuration object that holds Myracloud API credentials.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the Authenticator by calling the parent's init method."""
        super(Authenticator, self).__init__(*args, **kwargs)

    @classmethod
    def add_parser_arguments(cls, add: Callable, **kwargs):
        """
        Add custom arguments for the Myracloud DNS Authenticator.

        :param add: Callable to add an argument.
        :param kwargs: Additional keyword arguments.
        """
        super(Authenticator, cls).add_parser_arguments(
            add, default_propagation_seconds=900
        )
        add("credentials", help="Myracloud credentials INI file.")

    def _setup_credentials(self):
        """Set up and configure the Myracloud credentials."""
        self.credentials = self._configure_credentials(
            "credentials",
            "Myracloud credentials for the Myracloud DNS API",
            {
                "auth_token": "Defines the authentication token for the Myracloud DNS API.",
                "auth_secret": "Defines the authentication secret for the Myracloud DNS API."
            },
        )

    def _perform(self, domain: str, validation_name: str, validation: str):
        """
        Carry out a DNS update.

        :param domain: The domain where the DNS record will be added. Does not need to be the zone dns name but any domain.
        :param validation_name: The name of the DNS record.
        :param validation: The validation content to be added to the DNS record.
        """
        self._get_myracloud_client().add_txt_record(domain, validation_name, validation)

    def _cleanup(self, domain: str, validation_name: str, validation: str):
        """
        Remove the previously added DNS record.

        :param domain: The domain from which the DNS record will be deleted.
        :param validation_name: The name of the DNS record to be deleted.
        :param validation: The validation content of the DNS record to be deleted.
        """
        self._get_myracloud_client().del_txt_record(domain, validation_name, validation)

    def _get_myracloud_client(self) -> _MyracloudClient:
        """
        Instantiate and return a MyracloudClient object.

        :return: A _MyracloudClient instance to interact with the Myracloud DNS API.
        """
        return _MyracloudClient(
            self.credentials.conf("auth_token"),
            self.credentials.conf("auth_secret")
        )
