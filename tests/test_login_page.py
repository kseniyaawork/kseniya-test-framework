import pytest

from framework.config.config import TestData
from framework.pages.login_page import LoginPage


@pytest.mark.usefixtures("init_driver")
class TestLoginPage:
    def test_open_login_page(self):
        loginpage = LoginPage(self.driver)
        assert (
            loginpage.check_current_url()
            == "http://automationpractice.com/index.php?controller=authentication&back=my-account"
        )

    def test_login_page_title(self):
        loginpage = LoginPage(self.driver)
        assert loginpage.get_login_page_title() == "Login - My Store"

    def test_forgot_your_pass_link_visible(self):
        loginpage = LoginPage(self.driver)
        flag = loginpage.is_forgot_your_pass_link_exist()
        assert flag

    def test_login(self):
        loginpage = LoginPage(self.driver)
        loginpage.do_login(TestData.EMAIL, TestData.PASSWORD)

    def test_register(self):
        loginpage = LoginPage(self.driver)
        loginpage.create_account(TestData.EMAIL)
