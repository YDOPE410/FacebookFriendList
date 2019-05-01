from logger.txt_file_loger.txt_file_loger import Txt_file_logger as logger_class
from service.config_loader.json_config_loader.Json_config_loader import Json_config_loader
from constant import exit_code
from constant import selenium
from reporter.console_report.console_report import Console_reporter
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class Launcher:
    def _init(self):
        logger = logger_class()
        config = Json_config_loader.load("config_default.json")
        logger.set_log_lvl(config.log_lvl)
        logger.set_txt_file_path(config.path_to_save_logs)
        logger.console_handler(config.console_log)
        options = Options()
        options.add_argument('--no-sandbox')
        driver = None
        try:
            driver = webdriver.Chrome(executable_path=config.path_to_driver, options=options)
        except Exception as e:
            logger.fatal(f"{e}")
            exit(exit_code.BROWSER_ERROR)
        return config, driver, logger


    def _main(self, config, driver, logger):
        logger.debug(f"Opening {config.site}")
        driver.get(config.site)
        logger.debug(f"Finding login field")
        email = driver.find_element_by_name(selenium.email_field_name)
        logger.debug(f"Sending data to login field")
        email.send_keys(config.login)
        logger.debug("Finding password field")
        password = driver.find_element_by_name(selenium.password_field_name)
        logger.debug("Sending data to password field")
        password.send_keys(config.password)
        logger.debug("Click login button")
        driver.find_element_by_xpath(selenium.login_button_xpath).click()
        logger.debug("Finding profile link")
        driver.implicitly_wait(selenium.wait_time)
        profile = driver.find_element_by_xpath(selenium.profile_element_xpath)
        logger.debug("Click profile link")
        profile.send_keys(Keys.ENTER)
        driver.implicitly_wait(selenium.wait_time)
        logger.debug("Finding profile friends link")
        friends_link = driver.find_element_by_xpath(selenium.profile_friends_element_xpath)
        logger.debug("Click profile friends link")
        friends_link.send_keys(Keys.ENTER)
        driver.implicitly_wait(selenium.wait_time)
        logger.debug("Finding profile friend list")
        friends_a = driver.find_elements_by_css_selector(selenium.friends_a_css_selector)
        friends = dict()
        for friend in friends_a:
            friends[friend.text] = friend.get_attribute("href")
        return friends


    def _free(self, driver):
        driver.close()

    def _report(self, friends):
        Console_reporter.report(friends)

    def start(self):
        config, driver, logger = self._init()
        friends = self._main(config, driver, logger)
        self._report(friends)
        self._free(driver)


if __name__ == "__main__":
    launcher = Launcher()
    launcher.start()
