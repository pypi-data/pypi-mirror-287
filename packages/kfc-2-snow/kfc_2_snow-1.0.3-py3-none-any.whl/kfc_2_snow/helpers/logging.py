import logging
def setup_logging():
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("keyfactor_v_1_client").setLevel(logging.DEBUG)
    # format in syslog format
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    # create console handler and set level to info
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)
    # create file handler and set level to debug
    fileHandler = logging.FileHandler('snow_cert_import.log', "w")
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(formatter)
    logging.getLogger().addHandler(fileHandler)