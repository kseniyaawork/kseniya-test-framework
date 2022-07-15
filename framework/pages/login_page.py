from framework.config.config import TestData
from framework.pages.base_page import BasePage
from framework.pages.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    """constructor of the page class"""

    def __init__(self, driver):
        self.driver = driver
        self.driver.go_to_url(TestData.BASE_URL + "?controller=authentication&back=my-account")
        super().__init__(driver=driver)

    """Page actions for Login Page"""

    """this is used to get the page title"""

    def get_login_page_title(self):
        return self.get_title()

    def check_current_url(self):
        return self.check_url()

    """this is used to check forgot your pass link"""

    def is_forgot_your_pass_link_exist(self):
        return self.is_visible(LoginPageLocators.FORGOT_YOUR_PASS)

    """this is used to login to app"""

    def do_login(self, email, password):
        self.do_send_keys(LoginPageLocators.PASSWORD, password)
        self.do_send_keys(LoginPageLocators.EMAIL, email)
        self.do_click(LoginPageLocators.SIGNIN_BUTTON)

    """this is used to create a new account"""

    def create_account(self, email):
        self.do_send_keys(LoginPageLocators.EMAIL_FOR_REGESTRY, email)
        self.do_click(LoginPageLocators.CREATE_ACCOUNT_BUTTON)

    def get_login_value(self, by_locator):
        self.do_get_value(by_locator)
