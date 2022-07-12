import pytest
# from tests.kseniyaawork.framework.pages.login_page import LoginPage
from selenium import webdriver
from tests.kseniyaawork.framework.config.config import TestData
from tests.kseniyaawork.framework.pages.base_page import BasePage


class LoginPage(BasePage):

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        driver = self.driver
        self.driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
    def get_login_page_title(self):
        return self.get_title()

# @pytest.mark.usefixtures("init_driver")
class TestLoginPage:
    # driver = webdriver.Chrome()
    # def test_open_url(self):
    #     self.driver.get('https://www.google.by/')
    #     title = "Google"
    #     assert title == self.driver.title

    # def test_forgot_your_pass_link_visible(self):
    #     # driver = webdriver.Chrome() - с этой строкой работает, но нужно без нее
    #     self.loginPage = LoginPage(self.driver)
    #     flag = self.loginPage.is_forgot_your_pass_link_exist()
    #     assert flag
    @pytest.mark.usefixtures("init_driver")
    def test_login_page_title(self):
        # self.loginPage = LoginPage(self.driver)
        # self.loginPage = LoginPage(self.driver)
        self.title = LoginPage.get_login_page_title()
        assert self.title == "Login - My Store"

    # def test_login(self, init_driver):
    #     self.loginPage = LoginPage(self.driver)
    #     self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)


