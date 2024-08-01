# Certbot DNS-Myracloud Authenticator Plugin

The Certbot DNS-Myracloud Authenticator Plugin facilitates the procurement of SSL/TLS certificates from Let's Encrypt
utilizing the DNS-01 challenge methodology in conjunction with Myracloud as the designated DNS service provider. This
document elucidates the procedural steps for the installation and operational utilization of this plugin.

## Installation

To initialize the Certbot DNS-Myracloud Authenticator Plugin, deploy the following pip command:

```bash
pip install certbot-dns-myracloud
```

## Plugin Usage

Upon successful integration of the plugin, it becomes viable to employ it with Certbot for the retrieval of SSL/TLS
certificates. The subsequent section delineates the pertinent arguments and their respective examples:

### Arguments

| Argument                              | Example Value     | Description                                                                                                                                                                            |
|---------------------------------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--authenticator`                     | dns-myracloud     | Engages the Myracloud authenticator mechanism. This must be configured as dns-myracloud. (Mandatory)                                                                                   |
| `--dns-myracloud-credentials`         | ./credentials.ini | Denotes the directory path to the credentials file for Myracloud DNS. This document must encapsulate the dns_myracloud_auth_token and dns_myracloud_auth_secret variables. (Mandatory) |
| `--dns-myracloud-propagation-seconds` | 900               | Configures the delay prior to initiating the DNS record query. A 900-second interval (equivalent to 15 minutes) is recommended. (Default: 900)                                         |

### Example

Below is a structured example detailing the application of Certbot in conjunction with the DNS-Myracloud
Authenticator Plugin to retrieve a certificate:

```bash

# prepare environment
python3 -m venv e
. e/bin/activate

# install myracloud DNS authenticator
pip install certbot-dns-myracloud

# do not forget to have proper permissions set on your credentials.ini,
# like chmod 400 <path_to_credentials.ini>
# the auto

# retrieve cert
certbot certonly \
  --authenticator dns-myracloud \
  --dns-myracloud-credentials ./path_to_credentials.ini \
  --dns-myracloud-propagation-seconds 180 \
  --server https://acme-v02.api.letsencrypt.org/directory \
  --agree-tos \
  --elliptic-curve secp384r1 \
  --preferred-challenges dns \
  -d 'example.com' \
  -d '*.example.com'
```

For this example, example.com represents the designated domain (zone) for certificate procurement.

### Example of credentials.ini

To operationalize the plugin, it's imperative to curate a credentials.ini file encompassing your Myracloud DNS
credentials:

```ini
dns_myracloud_auth_token = "your_token_here"
dns_myracloud_auth_secret = "your_secret_here"
```

It's crucial to replace "your_token_here" and "your_secret_here" placeholders with the genuine Myracloud
authentication token and secret. The token's associated service account necessitates membership privileges
for record set creation.
