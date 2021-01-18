from pageObjects.LoginPage import  LoginPage
from utilities.ReadConfig import ReadConfig
from utilities.cusomLogger import LogGenerator
from selenium.webdriver.support.wait import WebDriverWait

class Test_login():

    logger = LogGenerator.setup_log()

    def test_login_page_load(self,access_login_page, browser,environment):
        """
        Test case to validate login page can be accessed
        :param access_login_page:
        :return: None
        """
        self.logger.info("Module-Login Test - Valdiate login page can be accessed")

        self.driver = access_login_page
        self.driver.get(ReadConfig.get_url())
        act_title = self.driver.title
        if act_title == "ToolsQA":
            assert True
            self.logger.info("Status- Passed")
        else:
            self.logger.error("Status- Failed")
            assert False
        self.driver.close()

    def test_validate_user_login(self,access_login_page, browser,environment):
        """
        Testcase to valdiate user can login with valid credentials
        :param access_login_page:
        :return:
        """
        self.logger.info("Module-Login Test - Valdiate user can login with valid credentials")

        self.driver = access_login_page
        self.driver.get(ReadConfig.get_url())
        obj_Login = LoginPage(self.driver)
        obj_Login.enter_user_id(ReadConfig.get_username())
        obj_Login.enter_password(ReadConfig.get_password())
        obj_Login.click_login()
        act_title = self.driver.title
        if act_title == "ToolsQA":
            assert True
            self.driver.close()
            self.logger.info("Status- Passed")
        else:
            self.driver.save_screenshot("test_validate_user_login.png")
            self.driver.close()
            self.logger.error("Status- Failed. Screenshot")
            assert False

    def test_login_fail_with_invalid_credentials(self, access_login_page, browser,environment):
        """
        Test case to validate if user cannot login with invalid credentials
        :param access_login_page:
        :param browser:
        :param environment:
        :return: NA
        """
        self.logger.info("Module-Login Test - Validate if user cannot login with invalid credentials")

        self.driver = access_login_page
        self.driver.get(ReadConfig.get_url())
        obj_Login = LoginPage(self.driver)
        obj_Login.enter_user_id("5345")
        obj_Login.enter_password("34533")
        obj_Login.click_login()
        element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(obj_Login.label_failedLoginMsg_id))
        self.driver.close()




