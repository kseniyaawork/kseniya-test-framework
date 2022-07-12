from tests.kseniyaawork.framework.config.config import TestData
from tests.kseniyaawork.framework.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from tests.kseniyaawork.framework.pages.login_page_locators import LoginPageLocators
from selenium import webdriver


class LoginPage(BasePage):
    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(TestData.BASE_URL + "http://automationpractice.com/index.php?controller=authentication&back=my-account")

    """Page actions for Login Page"""

    """this is used to get the page title"""

    def get_login_page_title(self):
        return self.get_title()

    """this is used to check forgot your pass link"""

    def is_forgot_your_pass_link_exist(self):
        return self.is_visible(LoginPageLocators.FORGOT_YOUR_PASS)

    """this is used to login to app"""

    def do_login(self, username, password):
        self.do_send_keys(LoginPageLocators.EMAIL, username)
        self.do_send_keys(LoginPageLocators.PASSWORD, password)
        self.do_click(LoginPageLocators.SIGNIN_BUTTON)


a = LoginPage(driver=webdriver.Chrome())


