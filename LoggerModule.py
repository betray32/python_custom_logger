import logging
import re

from SensitiveFormatter import SensitiveFormatter


class LoggerModule:

    # displayed format for logs
    log_format = "%(asctime)s — %(funcName)s:%(lineno)d — %(levelname)s — %(message)s"
    logger_instance = "MFS-Middleware - Service : login"

    # initial configuration
    def __init__(self):
        # create logger
        self.logger = logging.getLogger(self.logger_instance)
        self.logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        custom_handler_config = logging.StreamHandler()
        custom_handler_config.setLevel(logging.DEBUG)

        # create formatter and sensitive formatter
        sensitive_formatter = SensitiveFormatter(fmt=self.log_format)

        # add formatter to custom_handler_config
        custom_handler_config.setFormatter(sensitive_formatter)

        # add custom_handler_config to logger
        self.logger.addHandler(custom_handler_config)

    # get logger instance
    def get_logger(self):
        return self.logger
