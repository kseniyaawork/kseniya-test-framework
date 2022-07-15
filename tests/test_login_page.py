from framework.config.config import TestData
from framework.pages.login_page import LoginPage


class TestLoginPage:

    def test_open_login_page(self, init_driver):
        self.loginpage = LoginPage(self.driver)
        assert self.driver.current_url == "http://automationpractice.com/index.php?controller=authentication&back=my-account"

    def test_login_page_title(self, init_driver):
        self.loginPage = LoginPage(self.driver)
        self.title = self.loginPage.get_login_page_title()
        assert self.title == "Login - My Store"

    def test_forgot_your_pass_link_visible(self, init_driver):
        self.loginpage = LoginPage(self.driver)
        flag = self.loginpage.is_forgot_your_pass_link_exist()
        assert flag

    def test_login(self, init_driver):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)

    def test_register(self, init_driver):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.create_account(TestData.EMAIL)



