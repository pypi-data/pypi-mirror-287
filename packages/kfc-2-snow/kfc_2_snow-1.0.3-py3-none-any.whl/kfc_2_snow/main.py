import os
import requests
import json
import uuid
import logging
from datetime import datetime, timezone
from command_v11_client import keyfactor
from command_v11_client.models.csscms_data_model_models_certificate_retrieval_response import \
    CSSCMSDataModelModelsCertificateRetrievalResponse as KFCCertificate

from command_v11_client.models.csscms_data_model_models_certificate_retrieval_response_metadata import \
    CSSCMSDataModelModelsCertificateRetrievalResponseMetadata as KFCCertificateMetadata

from command_v11_client.models.csscms_data_model_models_certificate_retrieval_response_location_count_model import \
    CSSCMSDataModelModelsCertificateRetrievalResponseLocationCountModel as KFCCertificateLocationCount

from command_v11_client.models.keyfactor_web_keyfactor_api_models_certificates_certificate_recovery_request import \
    KeyfactorWebKeyfactorApiModelsCertificatesCertificateRecoveryRequest as KFCCertificateRecoveryRequest


LARGE_MAX_LENGTH = 10000
MAX_LENGTH = 4096


class KeyfactorSNOWDataManager:
    def __init__(self, **kwargs):
        logging.debug("Initializing KeyfactorSNOWDataManager")
        self.instance_url = kwargs.get("snow_url") or os.environ.get("SNOW_URL", 'https://ven06828.service-now.com')
        self.username = kwargs.get("snow_username") or os.environ.get("SNOW_USERNAME")
        self.password = kwargs.get("snow_password") or os.environ.get("SNOW_PASSWORD")
        
        self.import_set_table_name = kwargs.get("import_table_name") or 'kfc_certificate_import'
        self.import_table_label = kwargs.get("import_table_label") or "Keyfactor Command Certificate Import"
        
        self.sys_table_name = kwargs.get("sys_table_name") or "kfc_certificate_inventory"
        self.sys_table_label = kwargs.get("sys_table_label") or "Keyfactor Command Imported Certificate"
        self.sys_table_parent = kwargs.get("sys_table_parent") or "sys_import_set_row"

        self.app_prefix = kwargs.get("app_prefix") or os.environ.get("APP_PREFIX", "x_keyfa_app_")
        self.field_prefix = kwargs.get("field_prefix") or os.environ.get("FIELD_PREFIX", "kfc_")
        
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        logging.debug("Calling authenticate to ServiceNow instance %s", self.instance_url)
        self.snow_client = self.__authenticate()
        
        logging.debug("Successfully initialized KeyfactorSNOWDataManager")

        self.field_mappings = [
            ("cert_id", "u_cert_id"),
            ("certificate_b64", "u_certificate_b64"),
            ("certificate_pem", "u_certificate_pem"),
            ("expiry_date", "u_expiry_date"),
            ("has_private_key", "u_has_private_key"),
            ("is_expired", "u_is_expired"),
            ("issued_date", "u_issued_date"),
            ("issued_dn", "u_issued_dn"),
            ("issuer_dn", "u_issuer_dn"),
            ("location_count", "u_location_count"),
            ("locations", "u_locations"),
            ("metadata", "u_metadata"),
            ("private_key_bits", "u_private_key_bits"),
            ("private_key_type", "u_private_key_type"),
            ("sans", "u_sans"),
            ("serial_number", "u_serial_number"),
            ("thumbprint", "u_thumbprint"),
        ]
        self.dict_fields = [
            {
                "name": f"{self.field_prefix}cert_id",
                "label": "Certificate ID",
                "internal_type": "integer",
                "mandatory": True,
                "display": True,
                "primary": True,
                "unique": True
            },
            {
                "name": f"{self.field_prefix}certificate_b64",
                "label": "Certificate Base64 Encoded",
                "internal_type": "string",
                "mandatory": True,

                "display": False,
                "max_length": LARGE_MAX_LENGTH
            },
            {
                "name": f"{self.field_prefix}certificate_pem",
                "label": "Certificate PEM",
                "internal_type": "string",
                "mandatory": True,

                "display": True,
                "max_length": LARGE_MAX_LENGTH
            },
            {
                "name": f"{self.field_prefix}expiry_date",
                "internal_type": "glide_date_time",
                "label": "Expiry Date",
                "mandatory": True,

                "display": True,
            },
            {
                "name": f"{self.field_prefix}has_private_key",
                "internal_type": "boolean",
                "label": "Has Private Key",
                "mandatory": False,

                "display": True,
            },
            {
                "name": f"{self.field_prefix}is_expired",
                "internal_type": "boolean",
                "label": "Is Expired",
                "mandatory": False,

                "display": True,
            },
            {
                "name": f"{self.field_prefix}issued_date",
                "internal_type": "glide_date_time",
                "label": "Issued Date",
                "mandatory": True,

                "display": True,
            },
            {
                "name": f"{self.field_prefix}issued_dn",
                "internal_type": "string",
                "label": "Issued DN",
                "mandatory": True,

                "display": True,
                "max_length": MAX_LENGTH
            },
            {
                "name": f"{self.field_prefix}issued_cn",
                "internal_type": "string",
                "label": "Issued CN",
                "mandatory": False,
                "display": True,
                "max_length": MAX_LENGTH
            },
            {
                "name": f"{self.field_prefix}issuer_dn",
                "internal_type": "string",
                "label": "Issuer DN",
                "mandatory": True,
                "display": True,
                "max_length": MAX_LENGTH
            },
            {
                "name": f"{self.field_prefix}template_name",
                "internal_type": "string",
                "label": "Template Name",
                "mandatory": False,
                "display": True,
                "max_length": MAX_LENGTH
            },
            {
                "name": f"{self.field_prefix}location_count",
                "internal_type": "integer",
                "label": "Location Count",
                "mandatory": False,

                "display": True,
            },
            {
                "name": f"{self.field_prefix}locations",
                "internal_type": "string",
                "label": "Locations",
                "mandatory": False,

                "display": True,
                "max_length": LARGE_MAX_LENGTH
            },
            {
                "name": f"{self.field_prefix}metadata",
                "internal_type": "string",
                "label": "Metadata",
                "mandatory": False,

                "display": True,
                "max_length": LARGE_MAX_LENGTH
            },  # Storing as JSON string
            {
                "name": f"{self.field_prefix}private_key_bits",
                "internal_type": "integer",
                "label": "Private Key Bits",
                "mandatory": False,

                "display": True,
            },
            {
                "name": f"{self.field_prefix}private_key_type",
                "internal_type": "string",
                "label": "Private Key Type",
                "mandatory": False,

                "display": True,
                "max_length": MAX_LENGTH
            },
            {
                "name": f"{self.field_prefix}sans",
                "internal_type": "string",
                "label": "SANs",
                "mandatory": False,

                "display": True,
                "max_length": LARGE_MAX_LENGTH
            },  # Storing as JSON string
            {
                "name": f"{self.field_prefix}serial_number",
                "internal_type": "string",
                "label": "Serial Number",
                "mandatory": True,

                "display": True,
                "max_length": MAX_LENGTH
            },
            {
                "name": f"{self.field_prefix}thumbprint",
                "internal_type": "string",
                "label": "Thumbprint",
                "mandatory": True,

                "display": True,
                "max_length": MAX_LENGTH
            }
        ]
        self.data_source_sys_id = None
        self.transform_map_sys_id = None

    def __str__(self):
        return f"ServiceNow Instance: {self.instance_url}\n"

    def __authenticate(self):
        logging.debug("Authenticating to ServiceNow instance %s", self.instance_url)
        # create a session
        session = requests.Session()
        session.auth = (self.username, self.password)
        session.headers.update(self.headers)
        # attempt to make a request to the instance
        response = session.get(self.instance_url)
        response.raise_for_status()
        logging.debug("Successfully authenticated to ServiceNow instance %s", self.instance_url)
        return session

    def data_source_exists(self, name):
        url = f'{self.instance_url}/api/now/table/sys_data_source?name={name}'
        response = self.snow_client.get(url)
        response.raise_for_status()
        respJSON = response.json()
        logging.debug(f"Response: {respJSON}")
        results = respJSON.get('result', [])
        if results:
            return results[0]['sys_id']
        return None

    def create_data_source(self, import_table_name=None, import_set_table=None):
        if not import_table_name:
            import_table_name = self.import_table_label
        if not import_set_table:
            import_set_table = self.import_set_table_name
        existing_data_source = self.data_source_exists(import_table_name)
        if existing_data_source:
            logging.debug("Data source %s already exists in ServiceNow", import_table_name)
            return existing_data_source

        logging.debug("Creating data source in ServiceNow")
        url = f'{self.instance_url}/api/now/table/sys_data_source'
        data = {
            "name": f"{import_table_name}",
            "import_set_table_name": f"{import_set_table}",
            "type": "JSON",
            "format": "JSON",
            "file_retrieval_method": "Attachment",
            "jpath_root_node": "/"

        }
        logging.debug("Making POST request to ServiceNow to create data source %s", url)
        response = self.snow_client.post(url, data=json.dumps(data))
        response.raise_for_status()
        logging.debug("Data source %s successfully created in ServiceNow", import_set_table)
        respJson = response.json()
        logging.debug(f"Response: {respJson}")
        return response.json()['result']['sys_id']

    def upload_file(self, file_path, data_source_sys_id=None):
        if not data_source_sys_id:
            data_source_sys_id = self.data_source_sys_id
        logging.debug("Uploading file %s to ServiceNow data source %s", file_path, data_source_sys_id)
        url = f'{self.instance_url}/api/now/attachment/file?table_name=sys_data_source&table_sys_id={data_source_sys_id}&file_name=certificate_import.json'
        logging.debug("Attempting to open file %s", file_path)
        with open(file_path, 'rb') as file_data:
            logging.debug("Making POST request to ServiceNow to upload file %s", file_path)
            response = requests.post(url, files={'file': file_data})
        response.raise_for_status()
        logging.debug("File %s successfully uploaded to ServiceNow data source %s", file_path, data_source_sys_id)
        return response.json()['result']['sys_id']

    def load_data(self, data, import_set_table=None):
        output = []
        if not import_set_table:
            import_set_table = self.sys_table_name
        if isinstance(data, dict):
            data = [data]
        for item in data:
            logging.debug("Loading data into ServiceNow import set table %s", import_set_table)
            url = f'{self.instance_url}/api/now/import/{self.app_prefix}{import_set_table}'
            logging.debug("Making POST request to ServiceNow to load data into import set table %s", import_set_table)
            payload = {}
            for k, v in item.items():
                payload[f"{self.app_prefix}{self.field_prefix}{k}"] = v
            logging.debug("Payload: %s", payload)
            response = self.snow_client.post(url, json=payload)
            logging.debug("Response: %s", response.text)
            # response.raise_for_status()
            if response.status_code != 201:
                logging.error("Failed to load data into ServiceNow import set table %s", import_set_table)
                logging.error("Status Code: %s", response.status_code)
                logging.error("Response: %s", response.json())
                continue
                # return None
            respJSON = response.json()
            logging.debug("Response: %s", respJSON)
            logging.debug("Data successfully loaded into ServiceNow import set table %s", import_set_table)
            output.append(respJSON)
        return output

    def create_field_mapping(self, source_field, target_field, transform_map_sys_id=None):
        if not transform_map_sys_id:
            transform_map_sys_id = self.transform_map_sys_id
        logging.debug("Creating field mapping %s => %s in ServiceNow transform map %s", source_field, target_field,
                      transform_map_sys_id)
        url = f'{self.instance_url}/api/now/table/sys_transform_entry'
        data = {
            "map": transform_map_sys_id,
            "source_field": source_field,
            "target_field": target_field
        }
        logging.debug("Making POST request to ServiceNow to create field mapping %s => %s in transform map %s",
                      source_field,
                      target_field, transform_map_sys_id)
        response = self.snow_client.post(url, data=json.dumps(data))
        # response.raise_for_status()
        respJSON = response.json()
        if response.status_code != 201:
            logging.error("Failed to create field mapping %s => %s in ServiceNow transform map %s", source_field,
                          target_field, transform_map_sys_id)
            logging.error("Status Code: %s", response.status_code)
            logging.error("Response: %s", respJSON)
            return None

        logging.debug("Response: %s", respJSON)
        logging.debug("Field mapping %s => %s successfully created in ServiceNow transform map %s", source_field,
                      target_field, transform_map_sys_id)
        return response.json()['result']['sys_id']

    def transform_map_exists(self, name):
        url = f'{self.instance_url}/api/now/table/sys_transform_map?name={name}'
        response = self.snow_client.get(url)
        response.raise_for_status()
        results = response.json().get('result', [])
        if results:
            return results[0]['sys_id']
        return None

    def create_transform_map(self, import_table_name="", sys_table_name="", source_table=None):
        if not import_table_name:
            import_table_name = self.import_table_label
        if not sys_table_name:
            sys_table_name = self.sys_table_name
        if not source_table:
            source_table = self.import_set_table_name

        existing_sys_id = self.transform_map_exists(import_table_name)
        if existing_sys_id:
            logging.info("Transform map already exists in ServiceNow with sys_id %s", existing_sys_id)
            return existing_sys_id

        url = f'{self.instance_url}/api/now/table/sys_transform_map'
        data = {
            "name": f"{import_table_name}",
            "source_table": source_table,
            "target_table": sys_table_name,
        }
        response = self.snow_client.post(url, data=json.dumps(data))
        response.raise_for_status()
        respJSON = response.json()
        logging.debug("Response: %s", respJSON)
        logging.debug("Transform map successfully created in ServiceNow")
        return response.json()['result']['sys_id']

    def create_field_mappings(self, transform_map_sys_id="", field_mappings=None):
        if not transform_map_sys_id:
            transform_map_sys_id = self.transform_map_sys_id
        if not field_mappings:
            field_mappings = self.field_mappings
        for source_field, target_field in field_mappings:
            self.create_field_mapping(source_field, target_field, transform_map_sys_id)

    def sys_table_exists(self, name):
        logging.debug("Checking if table %s exists in ServiceNow", name)
        url = f'{self.instance_url}/api/now/table/sys_db_object'
        params = {'sysparm_query': f'name={name}'}  # todo: prefix param?
        response = self.snow_client.get(url, params=params)
        logging.debug("Response: %s", response.text)
        response.raise_for_status()
        respJSON = response.json()
        logging.debug("Response: %s", respJSON)
        results = respJSON.get('result', [])
        if results:
            return results[0]['sys_id']
        if self.app_prefix not in name:
            logging.debug("Table %s not found in ServiceNow, attempting to find table with app prefix", name)
            return self.sys_table_exists(f"{self.app_prefix}{name}")
        return None

    def create_sys_table(self, sys_table_name="", sys_table_label=""):
        if not sys_table_name:
            sys_table_name = self.sys_table_name
        if not sys_table_label:
            sys_table_label = self.sys_table_label
        existing_sys_id = self.sys_table_exists(sys_table_name)
        if existing_sys_id:
            logging.info("Table %s already exists in ServiceNow with sys_id '%s'", sys_table_name, existing_sys_id)
            self._add_systable_fields(table_name=sys_table_name)
            return existing_sys_id
        table_definition = {
            "name": f"{sys_table_name}",
            "label": f"{sys_table_label}",
            "super_class": self.sys_table_exists(self.sys_table_parent),
            "sys_scope": "global",
        }
        logging.info("Creating table %s in ServiceNow", sys_table_name)
        url = f'{self.instance_url}/api/now/table/sys_db_object'
        response = self.snow_client.post(url, data=json.dumps(table_definition))
        logging.debug("Response: %s", response.text)
        response.raise_for_status()
        respJSON = response.json()
        logging.debug("Response: %s", respJSON)
        sysId = respJSON['result']['sys_id']
        logging.info("Table '%s' successfully created in ServiceNow with sys_id '%s'", sys_table_name, sysId)
        self._add_systable_fields(table_name=sys_table_name)
        return sysId

    def _add_systable_fields(self, table_name: str, fields=None) -> str:
        logging.debug("Adding fields to table %s in ServiceNow", table_name)
        output = {}
        if not fields:
            fields = self.dict_fields
        for field in fields:
            field_name = field.get("name")
            try:
                logging.debug("Creating dictionary object %s and associating it with table %s in ServiceNow",
                              field_name, table_name)
                object_id = self.create_dictionary_object(table_name, field)
                output[field_name] = object_id
                logging.info("Dictionary object %s successfully created in ServiceNow", field['name'])
            except Exception as e:
                logging.error("Failed to create dictionary object %s in ServiceNow", field['name'], exc_info=True)
                output[field_name] = str(e)
                continue

    def dictionary_object_exists(self, table_name, field_name) -> str:
        url = f'{self.instance_url}/api/now/table/sys_dictionary'
        if self.app_prefix not in table_name:
            table_name = f"{self.app_prefix}{table_name}"
        
        params = {'sysparm_query': f'name={table_name}^element={field_name}'}
        response = self.snow_client.get(url, params=params)
        logging.debug("Response: %s", response.text)
        response.raise_for_status()
        respJSON = response.json()
        logging.debug("Response: %s", respJSON)
        results = respJSON.get('result', [])
        
        if results:
            return results[0]['sys_id']
        if self.app_prefix not in field_name:
            return self.dictionary_object_exists(table_name, f"{self.app_prefix}{field_name}")
        return ""

    def create_dictionary_object(self, table_name: str, field: dict) -> str:
        field_name = field.get("name")
        existing_sys_id = self.dictionary_object_exists(table_name, field_name)
        if existing_sys_id:
            logging.info("Dictionary object %s already exists in ServiceNow with sys_id '%s'", field_name,
                         existing_sys_id)
            return existing_sys_id

        url = f'{self.instance_url}/api/now/table/sys_dictionary'
        data = {
            "name": table_name,
            "element": field_name,
            "internal_type": field.get("internal_type"),
            # "sys_name": field.get("label"),
            "column_label": field.get("label"),
            "mandatory": field.get("mandatory", False),
            "read_only": field.get("read_only", False),
            "display": field.get("display", False),
            "primary": field.get("primary", False),
            "unique": field.get("unique", False),
            "max_length": field.get("max_length", 0),
        }
        response = self.snow_client.post(url, data=json.dumps(data))
        logging.debug("Response: %s", response.text)
        response.raise_for_status()
        respJSON = response.json()
        logging.debug("Response: %s", respJSON)
        return respJSON['result']['sys_id']

    def get_table_schema(self, table_name):
        url = f'{self.instance_url}/api/now/table/sys_db_object?sysparm_query=name={table_name}&sysparm_fields=sys_id'
        headers = {
            "Accept": "application/json"
        }
        response = self.snow_client.get(url)
        logging.debug("Response: %s", response.text)

        if response.status_code == 200:
            respJSON = response.json()
            logging.debug("Response: %s", respJSON)
            table_sys_id = respJSON['result'][0]['sys_id']
            url_fields = f'{self.instance_url}/api/now/table/sys_dictionary?sysparm_query=name={table_name}&sysparm_fields=element,internal_type'
            response_fields = self.snow_client.get(url_fields)
            logging.debug("Response: %s", response_fields.text)

            if response_fields.status_code == 200:
                respJSON = response_fields.json()
                logging.debug("Response: %s", respJSON)
                fields = response_fields.json()['result']
                field_definitions = [{"name": field["element"], "internal_type": field["internal_type"]} for field in
                                     fields]
                table_definition = {
                    "name": table_name,
                    "label": table_name,  # Adjust this if needed
                    "fields": field_definitions
                }
                return table_definition
            else:
                print(f'Error retrieving fields: {response_fields.status_code}')
                print(response_fields.json())
                return None
        else:
            print(f'Error retrieving table: {response.status_code}')
            print(response.json())
            return None

    def create_import_set_table(self, table_name=None, import_set_table_name=None):
        if not table_name:
            table_name = self.import_table_label
        if not import_set_table_name:
            import_set_table_name = self.import_set_table_name

        logging.debug("Making POST request to ServiceNow to create data source table %s", table_name)
        url = f'{self.instance_url}/api/now/table/sys_data_source'
        response = self.snow_client.post(
            url,
            data={
                "name": f"{table_name}",
                "import_set_table_name": f"{import_set_table_name}",
                "type": "JSON",
                "format": "JSON",
                "file_retrieval_method": "Attachment"
            }
        )

        if response.status_code == 201:
            logging.info('Import set table schema successfully created in ServiceNow.')
            logging.debug(f'Response: {response.json()}')
        else:
            logging.error('Failed to create import set table schema in ServiceNow.')
            logging.error(f'Status Code: {response.status_code}')
            logging.error(f'Response: {response.json()}')

    def add_data(self):
        data = {
            "store_id": str(uuid.uuid4()),
            "inventory": [
                {"cert_id": 1, "thumbprint": "sample_thumbprint_1", "alias": "sample_alias_1"},
                {"cert_id": 2, "thumbprint": "sample_thumbprint_2", "alias": "sample_alias_2"}
            ]
        }

        json_data = json.dumps(data)

        api_endpoint = f'{self.instance_url}/api/now/table/x_keyfa_app_u_store_inventory_import'

        response = requests.post(api_endpoint, auth=(self.username, self.password), headers=self.headers,
                                 data=json_data)

        if response.status_code == 201:
            logging.info('Data successfully imported into ServiceNow.')
            logging.debug(f'Response: {response.json()}')
        else:
            logging.error('Failed to import data into ServiceNow.')
            logging.error(f'Status Code: {response.status_code}')
            logging.error(f'Response: {response.json()}')

    def format_certs(self, certs: [KFCCertificate]) -> [dict]:
        output = []
        for cert in certs:
            output.append(json.loads(KeyfactorSNOWCertificate(cert).toJSON()))
        return output

    def list_kfc_certificates(self) -> [dict]:
        logging.debug("Retrieving certificates from Keyfactor Command")
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
        logging.debug("Retrieved %d certificates from Keyfactor Command", len(certs))
        output = self.format_certs(certs)

        return output


class KeyfactorSNOWCertificate:
    def __init__(self, cert: KFCCertificate):
        logging.debug(f"Processing certificate: {cert.id}")
        self.cert_id = cert.id
        self.thumbprint = cert.thumbprint
        self.serial_number = cert.serial_number
        self.metadata = self.process_metadata(cert.metadata)
        self.locations = self.process_locations(cert.locations)
        self.location_count = self.process_location_counts(cert.locations_count)
        self.has_private_key = cert.has_private_key
        self.issued_cn = cert.issued_cn
        self.issued_dn = cert.issued_dn
        self.issuer_dn = cert.issuer_dn
        self.template_name = cert.template_name
        if self.has_private_key:
            self.private_key_type = cert.key_type
            self.private_key_bits = cert.key_size_in_bits
        else:
            self.private_key_type = ""
            self.private_key_bits = 0
        self.sans = []
        if cert.subject_alt_name_elements:
            for san in cert.subject_alt_name_elements:
                self.sans.append(san.value)
        self.sans = json.dumps(self.sans)
        self.issued_date = cert.not_before
        self.expiry_date = cert.not_after
        self.is_expired = datetime.now(timezone.utc) > self.expiry_date
        self.certificate_b64 = cert.content_bytes
        logging.debug(f"Processed certificate: {self.cert_id}")
        self.certificate_pem = self.to_pem()



    def get_private_key(self):
        if self.has_private_key:
            request = KFCCertificateRecoveryRequest(
                thumbprint=self.thumbprint,
                password="arandomPassword123!@#",
                include_chain=True,
                chain_order="",
                use_legacy_encryption=False,
                cert_id=self.cert_id
            )
            return keyfactor.post_certificates_recover_(
                json_body=request
            )
        return None

    def to_pem(self, include_private_key=False):
        logging.debug("Converting certificate to PEM format")
        header = "-----BEGIN CERTIFICATE-----\n"
        footer = "\n-----END CERTIFICATE-----"

        # Split the string into lines of 64 characters each
        pem_body = "\n".join([self.certificate_b64[i:i + 64] for i in range(0, len(self.certificate_b64), 64)])

        # Combine header, body, and footer
        pem_formatted = header + pem_body + footer

        if include_private_key:
            logging.debug("Attempting to recover private key")
            # TODO: SDK error :"{"ErrorCode":"0xA0110007","Message":"You must supply a certificate format in the 'X-CertificateFormat' header of the request."}"
        #     private_key = self.get_private_key()
        #     if private_key:
        #         pem_formatted += f"\n\n-----BEGIN PRIVATE KEY-----\n"
        #         pem_formatted += private_key
        #         pem_formatted += f"\n-----END PRIVATE KEY

        logging.debug("Converted certificate to PEM format")
        return pem_formatted

    def process_location_counts(self, location_counts: KFCCertificateLocationCount) -> int:
        output = 0
        for location_count in location_counts:
            output += location_count.count
        return output

    def process_metadata(self, metadata: KFCCertificateMetadata) -> str:
        output = {}

        if not metadata.additional_properties and not metadata.additional_keys:
            return ""

        for key in metadata.additional_keys:
            output[key] = metadata.additional_properties[key]

        return json.dumps(output)

    def process_locations(self, locations=None) -> str:
        output = set()
        if not locations:
            return ""
        for location in locations:
            # if not (output.get(location.store_path)):
            #     output[location.store_path] = []
            # output[location.store_path].append(location.alias)
            output.add(f"{location.store_path}: {location.alias}")
        return ",\n".join(sorted(output))

    def __str__(self):
        return f"Cert ID: {self.cert_id}, Thumbprint: {self.thumbprint}"

    def toJSON(self):
        def default(o):
            if isinstance(o, datetime):
                return o.isoformat()
            return o.__dict__

        return json.dumps(self, default=default, sort_keys=True, indent=4)

    def toCSV(self):
        header = ["cert_id", "thumbprint", "serial_number",
                  "has_private_key",
                  "issued_dn", "issuer_dn", "private_key_type", "private_key_bits", "issued_date",
                  "expiry_date",
                  "is_expired", "certificate_b64", "certificate_pem"]
        data = [self.cert_id, self.thumbprint, self.serial_number,
                self.has_private_key, self.issued_dn, self.issuer_dn, self.private_key_type, self.private_key_bits,
                self.issued_date, self.expiry_date, self.is_expired, self.certificate_b64,
                self.certificate_pem]
        return data


# setup_logging()
# snow_manager = KeyfactorSNOWDataManager()
# sys_table_id = snow_manager.create_sys_table()
# data_source_sys_id = snow_manager.create_data_source()
# transform_map_sys_id = snow_manager.create_transform_map()
# snow_manager.create_field_mappings(transform_map_sys_id=transform_map_sys_id)

# certs = snow_manager.list_kfc_certificates()
# snow_manager.load_data(certs)

# read in certificates.json and load data into ServiceNow
# with open("certificates.json", "r") as cert_file:
#     data = json.load(cert_file)
#     data_obj = {
#         "certificates": data
#     }
#     snow_manager.load_data(data)
