from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.kseniyaawork.framework.tests import conftest


class BasePage:
    """
    This class is the parent for all pages.
    It contains all general methods for all pages.
    """

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        self.driver.implicitly_wait(10)
        by_locator.click()

    def do_send_keys(self, by_locator, text):
        self.driver.implicitly_wait(10)
        by_locator.send_keys(text)

    def get_element_keys(self, by_locator):
        element = by_locator
        return element.text

    def is_visible(self, by_locator):
        element = by_locator
        return bool(element)

    def get_title(self):
        return self.driver.title
