from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


class Driver:
    """
    An object that represents the driver powering the tasks.
    """

    def __init__(self, url: str) -> None:
        """
        :param url: The URL to start the driver on.
        """
        self.url = url
        self.driver = self.get_chrome_webdriver()
        self.driver.set_window_size(1920, 1080)
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.search = WebDriverWait(self.driver, 30)

    def close_and_quit(self) -> None:
        """
        Closes and quits the driver.
        """
        self.driver.close()
        self.driver.quit()

    def go_to_url(self, url: str) -> None:
        """
        Goes to the given URL.

        :param url: The URL to go to.
        """
        self.driver.get(url=url)

    @staticmethod
    def get_chrome_webdriver() -> WebDriver:
        """
        Creates a Chrome based WebDriver object.

        :return: An instance of the Chrome WebDriver.
        """
        chrome_options = Driver._get_chrome_options()
        return webdriver.Chrome(options=chrome_options)

    @staticmethod
    def _get_chrome_options():
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-setuid-sandbox")
        return options

    def custom_get_title(self):
        return self.driver.title

    def custom_current_url(self):
        return self.driver.current_url

    @staticmethod
    def custom_is_visible(by_locator):
        element = by_locator
        return bool(element)

    def custom_send_keys(self, locator: tuple, text):
        elt = self.driver.find_element(By.XPATH, locator)
        elt.send_keys(text)

    def custom_click(self, locator: tuple):
        elt = self.driver.find_element(By.XPATH, locator)
        elt.click()

    def custom_get_value(self, locator: tuple):
        element = self.driver.find_element(By.XPATH, locator)
        return element.get_attribute("value")
