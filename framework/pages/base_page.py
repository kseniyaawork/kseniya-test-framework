class BasePage:
    """
    This class is the parent for all pages.
    It contains all general methods for all pages.
    """

    def __init__(self, driver):
        self.driver = driver

    def do_send_keys(self, by_locator, text):
        return self.driver.custom_send_keys(by_locator, text)

    def do_click(self, by_locator):
        return self.driver.custom_click(by_locator)

    def do_get_value(self, by_locator):
        return self.driver.custom_get_value(by_locator)

    @staticmethod
    def get_element_keys(by_locator):
        element = by_locator
        return element.text

    def is_visible(self, by_locator):
        return self.driver.custom_is_visible(by_locator)

    def get_title(self):
        return self.driver.custom_get_title()

    def check_url(self):
        return self.driver.custom_current_url()
