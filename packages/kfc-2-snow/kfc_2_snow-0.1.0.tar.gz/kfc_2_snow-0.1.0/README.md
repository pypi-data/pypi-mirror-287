# kfc2snow

This is a simple CLI that can be used to facilitate importing data from a Keyfactor Command Instance into a ServiceNow
instance.

## Installation

### From Source

1. Clone the repository
2. Install `poetry`: `pip install --upgrade pip && pip install poetry`
3. Install dependencies: `poetry install`
4. Run the CLI: `kfc2snow --help`

```bash
git clone https://github.com/Keyfactor/kfc-inv-2-snow.git
cd kfc-inv-2-snow
pip install --upgrade pip && pip install poetry
poetry install
poetry run pip install .
poetry run kfc2snow --help
```

## Usage

### Environment Variables

You can use the following environmental variables to authenticate with Keyfactor Command and ServiceNow while using the
`kfc2snow` CLI.

#### Keyfactor Command AD/Basic Auth

Below is an example of how to set the environment variables for Keyfactor Command using AD/Basic Auth.

```bash
export KEYFACTOR_HOSTNAME=keyfactor.example.com
export KEYFACTOR_USERNAME=User
export KEYFACTOR_PASSWORD=MyPassword
export KEYFACTOR_DOMAIN=EXAMPLEDOMAIN
export SNOW_INSTANCE=https://example.service-now.com
export SNOW_USERNAME=MySnowUser
export SNOW_PASSWORD=MySnowPassword
```

#### Keyfactor Command OAuth Identity Provider

Below is an example of how to set the environment variables for Keyfactor Command using an OAuth identity provider.

```bash
export KEYFACTOR_HOSTNAME=keyfactor.example.com
export COMMAND_IDP_TOKENURL=https://<idp host>/realms/<realm_name>/protocol/openid-connect/token
export COMMAND_IDP_CLIENTID=MyOauthCilentId
export COMMAND_IDP_CLIENTSECRET=MyOauthClientSecret
export SNOW_INSTANCE=https://example.service-now.com
export SNOW_USERNAME=MySnowUser
export SNOW_PASSWORD=MySnowPassword
```

#### Full Example

Below is an example of how to set the environment variables for Keyfactor Command using AD/Basic Auth and doing a "full"
deployment and import to ServiceNow.

```bash
kfc2snow create-tables \
    --keyfactor-hostname keyfactor.example.com \
    --keyfactor-username User \
    --keyfactor-password MyPassword \
    --keyfactor-domain EXAMPLEDOMAIN \
    --snow-url https://example.service-now.com \
    --snow-username MySnowUser \
    --snow-password MySnowPassword

kfc2snow import-certs \
    --keyfactor-hostname keyfactor.example.com \
    --keyfactor-username User \
    --keyfactor-password MyPassword \
    --keyfactor-domain EXAMPLEDOMAIN \
    --snow-url https://example.service-now.com \
    --snow-username MySnowUser \
    --snow-password MySnowPassword
```

### Commands

#### `create-tables`

This command will create the necessary tables in ServiceNow for the import process.

```text
kfc2snow create-tables --help
Usage: kfc2snow create-tables [OPTIONS]

  Create a ServiceNow table for certificates

Options:
  --keyfactor-hostname TEXT       Keyfactor instance hostname
  --keyfactor-username TEXT       Keyfactor username
  --keyfactor-password TEXT       Keyfactor password
  --keyfactor-domain TEXT         Keyfactor domain (if using AD auth)
  --command-idp-tokenurl TEXT     IDP token URL (if using OAuth2)
  --command-idp-clientid TEXT     OAuth2 client ID
  --command-idp-clientsecret TEXT
                                  OAuth2 client secret
  --snow-url TEXT                 ServiceNow instance URL
  --snow-username TEXT            ServiceNow username
  --snow-password TEXT            ServiceNow password
  --app-prefix TEXT               Application prefix (optional)
  --field-prefix TEXT             Field prefix (optional)
  --import-table-name TEXT        The system name of the `import table` to
                                  create in Service Now (optional)
  --import-table-label TEXT       The canonical name/label of the `import
                                  table` to create in Service Now (optional)
  --sys-table-name TEXT           The system name of the `sys table` to create
                                  in Service Now (optional)
  --sys-table-label TEXT          The canonical name/label of the `sys table`
                                  to create in Service Now (optional)
  --sys-table-parent TEXT         The sys name of the `sys table` to base the
                                  `sys table` on in Service Now (optional)
  --help                          Show this message and exit.
```

Here's what the table can look like in ServiceNow:
![snow_import_table.png](docs%2Fimages%2Fsnow_import_table.png)

##### bash
Example with all fields specified:
```bash
kfc2snow create-tables \
    --keyfactor-hostname $KEYFACTOR_HOSTNAME \
    --keyfactor-username $KEYFACTOR_USERNAME \
    --keyfactor-password $KEYFACTOR_PASSWORD \
    --keyfactor-domain $KEYFACTOR_DOMAIN \
    --snow-url $SNOW_URL \
    --snow-username $SNOW_USERNAME \
    --snow-password $SNOW_PASSWORD \
    --app-prefix "x_keyfa_app_" \
    --field-prefix "kfc_" \
    --import-table-name "certificates_import" \
    --import-table-label "Keyfactor Command Certificate Import" \
    --sys-table-name "certificate_inventory" \
    --sys-table-label "Keyfactor Command Certificates"
```

#### `import-certs`

This command will import certificates from Keyfactor Command into ServiceNow.

```text
kfc2snow import-certs --help
Usage: kfc2snow import-certs [OPTIONS]

  Import certificates into ServiceNow

Options:
  --keyfactor-hostname TEXT       Keyfactor instance hostname
  --keyfactor-username TEXT       Keyfactor username
  --keyfactor-password TEXT       Keyfactor password
  --keyfactor-domain TEXT         Keyfactor domain (if using AD auth)
  --command-idp-tokenurl TEXT     IDP token URL (if using OAuth2)
  --command-idp-clientid TEXT     OAuth2 client ID
  --command-idp-clientsecret TEXT
                                  OAuth2 client secret
  --snow-url TEXT                 ServiceNow instance URL
  --snow-username TEXT            ServiceNow username
  --snow-password TEXT            ServiceNow password
  --app-prefix TEXT               Application prefix (optional)
  --field-prefix TEXT             Field prefix (optional)
  --import-table-name TEXT        The system name of the `import table` to
                                  create in Service Now (optional)
  --import-table-label TEXT       The canonical name/label of the `import
                                  table` to create in Service Now (optional)
  --sys-table-name TEXT           The system name of the `sys table` to create
                                  in Service Now (optional)
  --sys-table-label TEXT          The canonical name/label of the `sys table`
                                  to create in Service Now (optional)
  --sys-table-parent TEXT         The sys name of the `sys table` to base the
                                  `sys table` on in Service Now (optional)
  --help                          Show this message and exit.
```

Here's what imported certificate data can look like in ServiceNow:
![kfc_inv_snow_import_rows.png](docs%2Fimages%2Fkfc_inv_snow_import_rows.png)

##### bash
Example with all fields specified:
```bash
kfc2snow import-certs \
    --keyfactor-hostname $KEYFACTOR_HOSTNAME \
    --keyfactor-username $KEYFACTOR_USERNAME \
    --keyfactor-password $KEYFACTOR_PASSWORD \
    --keyfactor-domain $KEYFACTOR_DOMAIN \
    --snow-url $SNOW_URL \
    --snow-username $SNOW_USERNAME \
    --snow-password $SNOW_PASSWORD \
    --app-prefix "x_keyfa_app_" \
    --field-prefix "kfc_" \
    --import-table-name "certificates_import" \
    --import-table-label "Keyfactor Command Certificate Import" \
    --sys-table-name "certificate_inventory" \
    --sys-table-label "Keyfactor Command Certificates"
```



## Debugging
To enable debugging, set the `DEBUG` environment variable to `1` or pass the `--debug` flag to the CLI.

```bash
kfc2snow --debug create-tables
kfc2snow --debug import-certs
```