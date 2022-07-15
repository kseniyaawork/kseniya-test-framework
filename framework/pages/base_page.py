from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    This class is the parent for all pages.
    It contains all general methods for all pages.
    """

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).click()


    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
    
    def get_element_keys(self, by_locator):
        element = by_locator
        return element.text

    def is_visible(self, by_locator):
        element = by_locator
        return bool(element)

    def get_title(self):
        return self.driver.title
