from service.config_loader.config_loader import Config_loader
import json
from config.configuration import Configuration
from logger.txt_file_loger.txt_file_loger import Txt_file_logger
from constant.exit_code import *
from constant import config_default


class Json_config_loader(Config_loader):

    @staticmethod
    def load(path):
        logger = Txt_file_logger()

        try:
            with open(path) as json_file:
                config = Configuration(**json.load(json_file))
        except OSError:
            logger.error(f"Can`t load config {path}")

        return Json_config_loader._verify(config)


    @staticmethod
    def _verify(config):
        logger = Txt_file_logger()
        if type(config.site) != str or config.site == "" or not config.site =="http://www.facebook.com":
            logger.debug(f"Config. Set default site {config_default.site}")
            config.site = config_default.site
        if type(config.password) != str or config.password == "":
            logger.error("Config. Incorrect password")
            exit(PASSWORD_FIELD_ERROR)
        if type(config.login) != str or config.login == "":
            logger.error("Config. Incorrect login")
            exit(LOGIN_FIELD_ERROR)
        if type(config.log_lvl) != int and not (0 < config.log_lvl > 7):
            logger.debug(f"Config. Set default log_lvl {config_default.log_lvl}")
            config.log_lvl = config_default.log_lvl
        if type(config.console_log) != bool:
            logger.debug(f"Config. Set default console log bool {config_default.console_log}")
            config.console_log = config_default.console_log
        if type(config.path_to_driver) != str or config.path_to_driver == "":
            logger.debug(f"Config. Set default path to driver {config_default.path_to_driver}")
            config.path_to_driver = config_default.path_to_driver
        if type(config.path_to_save_logs) != str or config.path_to_save_logs == "":
            logger.debug(f"Config. Set default path to save logs {config_default.path_to_save_logs}")
            config.path_to_save_logs = config_default.path_to_save_logs

        return config
