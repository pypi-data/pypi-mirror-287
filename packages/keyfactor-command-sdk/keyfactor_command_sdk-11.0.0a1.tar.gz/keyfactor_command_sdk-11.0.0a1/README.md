ALPHA build/internal testing only:

SDK in Python for Command 11.2 Web APIs. Compatible with both AD auth and OAuth, though this is NOT supported in any capacity and NOT rigorously tested.

Setup:
1. Clone this repo.
2. Set environment variables as per one of the examples below.
3. Change directory to the repo root and run python.
4. Import keyfactor.

Authentication options:
```
export KEYFACTOR_HOSTNAME=keyfactor.example.com
export KEYFACTOR_USERNAME=User
export KEYFACTOR_PASSWORD=MyPassword
export KEYFACTOR_DOMAIN=EXAMPLEDOMAIN
```

OR

```
export KEYFACTOR_HOSTNAME=kftrain.keyfactor.lab
export COMMAND_IDP_TOKENURL=https://<idp host>/realms/Keyfactor/protocol/openid-connect/token
export COMMAND_IDP_CLIENTID=MyIdpCilent
export COMMAND_IDP_CLIENTSECRET=MyClientSecret
```

Usage:
```
>>> keyfactor.get_metadata_fields_()

[CSSCMSDataModelModelsMetadataFieldTypeModel(id=1, name='Email-Contact', description='Email contact for the certificate.',
```

```
>>> keyfactor.enrollment_pfx({"subject":"CN=foo","template":"WebServer","timestamp":"2024-04-02T18:00:00Z","certificate_authority":"mycahost\\MyCALogicalName"})

{'certificateInformation': {'keyfactorRequestId': 0, 'requestDisposition': 'ISSUED', 'dispositionMessage': 'The template was not set up for private key retention, so no private key was saved.', 'enrollmentContext': None, 'keyfactorId': 64478, 'pkcs12Blob': 'MIIL7...
```

## Quickstart

### Installation
```bash
git clone https://github.com/Keyfactor/command-11-python-client-sdk.git
pip install .
```

### Environment Variables
```bash
export KEYFACTOR_HOSTNAME=keyfactor.example.com
export KEYFACTOR_USERNAME=User
export KEYFACTOR_PASSWORD=MyPassword
export KEYFACTOR_DOMAIN=EXAMPLEDOMAIN
````

### Usage

```python
from command_v11_client import keyfactor

certs = []
index = 1  # Start at page 1 as any page <1 will return the results of page 1
while (c := keyfactor.get_certificates_(
        include_locations=True,
        include_metadata=True,
        include_has_private_key=True,
        page_returned=index
)):
    certs.extend(c)
    index += 1

for cert in certs:
    print(cert)
```