import os
import click
from kfc_2_snow.helpers.logging import setup_logging
from kfc_2_snow.main import KeyfactorSNOWDataManager


def common_options(func):
    options = [
        click.option('--keyfactor-hostname', envvar='KEYFACTOR_HOSTNAME',
                     help="Keyfactor instance hostname"),
        click.option('--keyfactor-username', envvar='KEYFACTOR_USERNAME', help="Keyfactor username"),
        click.option('--keyfactor-password', envvar='KEYFACTOR_PASSWORD', help="Keyfactor password"),
        click.option('--keyfactor-domain', envvar='KEYFACTOR_DOMAIN', help="Keyfactor domain (if using AD auth)"),
        click.option('--command-idp-tokenurl', envvar='COMMAND_IDP_TOKENURL', help="IDP token URL (if using OAuth2)"),
        click.option('--command-idp-clientid', envvar='COMMAND_IDP_CLIENTID', help="OAuth2 client ID"),
        click.option('--command-idp-clientsecret', envvar='COMMAND_IDP_CLIENTSECRET', help="OAuth2 client secret"),
        click.option('--snow-url', envvar='SNOW_URL', help="ServiceNow instance URL"),
        click.option('--snow-username', envvar='SNOW_USERNAME', help="ServiceNow username"),
        click.option('--snow-password', envvar='SNOW_PASSWORD', help="ServiceNow password"),
        click.option('--app-prefix', envvar='APP_PREFIX', default='x_keyfa_app_', help="Application prefix (optional)"),
        click.option('--field-prefix', envvar='FIELD_PREFIX', default='kfc_', help="Field prefix (optional)"),
        click.option('--import-table-name', envvar='SNOW_IMPORT_TABLE_NAME',
                     help="The system name of the `import table` to create in Service Now (optional)"),
        click.option('--import-table-label', envvar='SNOW_IMPORT_TABLE_LABEL',
                     help="The canonical name/label of the `import table` to create in Service Now (optional)"),
        click.option('--sys-table-name', envvar='SNOW_SYS_TABLE_NAME',
                     help="The system name of the `sys table` to create in Service Now (optional)"),
        click.option('--sys-table-label', envvar='SNOW_SYS_TABLE_LABEL',
                     help="The canonical name/label of the `sys table` to create in Service Now (optional)"),
        click.option('--sys-table-parent', envvar='SNOW_SYS_TABLE_PARENT', default="sys_import_set_row",
                     help="The sys name of the `sys table` to base the `sys table` on in Service Now (optional)", ),

    ]
    for option in reversed(options):
        func = option(func)
    return func


@click.group()
@click.option('--debug', is_flag=True, help="Enable debug logging")
def cli(debug):
    """Keyfactor ServiceNow Data Manager CLI"""
    if debug:
        setup_logging()


@click.command()
def show_setup():
    """Prints out detailed information about environment setup and usage of the CLI."""
    help_text = """
    Keyfactor ServiceNow Data Manager CLI

    Environment Setup: https://software.keyfactor.com/Core-OnPrem/Current/Content/WebAPI/AuthenticateAPI.htm
    Keyfactor Command AD/Basic Auth:
        - `KEYFACTOR_HOSTNAME`: Keyfactor instance hostname (e.g., 'https://your_instance.keyfactor.com')
        - `KEYFACTOR_USERNAME`: If using AD/Basic auth, set the username
        - `KEYFACTOR_PASSWORD`: If using AD/Basic auth, set the password
        - `KEYFACTOR_DOMAIN`: If using AD auth, set the domain it not included in username
    keyfactor Command OAuth2 Auth: 
        - `KEYFACTOR_HOSTNAME`: Keyfactor instance hostname (e.g., 'https://your_instance.keyfactor.com')
        - `COMMAND_IDP_TOKENURL`: https://<idp host>/realms/<realm>/protocol/openid-connect/token
        - `COMMAND_IDP_CLIENTID`: oauth2 client id
        - `COMMAND_IDP_CLIENTSECRET`: oauth2 client secret
    Service Now:
        - `SNOW_URL`: ServiceNow instance URL (e.g., 'https://your_instance.service-now.com')
        - `SNOW_USERNAME`: ServiceNow username
        - `SNOW_PASSWORD`: ServiceNow password
        - `APP_PREFIX`: (Optional) Application prefix, default is 'x_keyfa_app_'
        - `FIELD_PREFIX`: (Optional) Field prefix, default is 'kfc_'
    """
    click.echo(help_text)


@click.command()
@common_options
def create_tables(
        keyfactor_hostname, keyfactor_username, keyfactor_password, keyfactor_domain,
        command_idp_tokenurl, command_idp_clientid, command_idp_clientsecret, snow_url, snow_username,
        snow_password, app_prefix, field_prefix, import_table_name, import_table_label, sys_table_name,
        sys_table_label, sys_table_parent):
    """Create a ServiceNow table for certificates"""
    snow_manager = KeyfactorSNOWDataManager(
        keyfactor_hostname=keyfactor_hostname,
        keyfactor_username=keyfactor_username,
        keyfactor_password=keyfactor_password,
        keyfactor_domain=keyfactor_domain,
        command_idp_tokenurl=command_idp_tokenurl,
        command_idp_clientid=command_idp_clientid,
        command_idp_clientsecret=command_idp_clientsecret,
        snow_url=snow_url,
        snow_username=snow_username,
        snow_password=snow_password,
        app_prefix=app_prefix,
        field_prefix=field_prefix,
        import_table_name=import_table_name,
        import_table_label=import_table_label,
        sys_table_name=sys_table_name,
        sys_table_label=sys_table_label,
        sys_table_parent=sys_table_parent
    )
    sys_table_id = snow_manager.create_sys_table()
    click.echo(f"ServiceNow table created with sys_id: {sys_table_id}")


@click.command()
@common_options
def import_certs(
        keyfactor_hostname, keyfactor_username, keyfactor_password, keyfactor_domain, command_idp_tokenurl,
        command_idp_clientid, command_idp_clientsecret, snow_url, snow_username, snow_password, app_prefix,
        field_prefix, import_table_name, import_table_label, sys_table_name,
        sys_table_label, sys_table_parent):
    """Import certificates into ServiceNow"""
    snow_manager = KeyfactorSNOWDataManager(
        keyfactor_hostname=keyfactor_hostname,
        keyfactor_username=keyfactor_username,
        keyfactor_password=keyfactor_password,
        keyfactor_domain=keyfactor_domain,
        command_idp_tokenurl=command_idp_tokenurl,
        command_idp_clientid=command_idp_clientid,
        command_idp_clientsecret=command_idp_clientsecret,
        snow_url=snow_url,
        snow_username=snow_username,
        snow_password=snow_password,
        app_prefix=app_prefix,
        field_prefix=field_prefix,
        import_table_name=import_table_name,
        import_table_label=import_table_label,
        sys_table_name=sys_table_name,
        sys_table_label=sys_table_label,
        sys_table_parent=sys_table_parent

    )
    certs = snow_manager.list_kfc_certificates()
    output = snow_manager.load_data(certs)
    click.echo("Certificates imported into ServiceNow")
    click.echo(output)


cli.add_command(show_setup)
cli.add_command(create_tables)
cli.add_command(import_certs)

if __name__ == "__main__":
    cli()
