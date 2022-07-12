from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

from framework.common.env_vars import should_run_headless


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

    def switch_to_default_content(self) -> None:
        """
        Switches the driver back to the main content in the DOM tree.
        """
        self.driver.switch_to.default_content()

    def switch_to_frame(self, name: str) -> None:
        """
        Switches the driver the a frame with the given name.

        :param name: The frame name.
        """
        self.driver.switch_to.frame(frame_reference=name)

    @staticmethod
    def get_chrome_webdriver() -> WebDriver:
        """
        Creates a Chrome based WebDriver object.

        :return: An instance of the Chrome WebDriver.
        """
        chrome_options = Driver._get_chrome_options()
        return webdriver.Chrome(options=chrome_options)

    @staticmethod
    def _get_chrome_options() -> webdriver.ChromeOptions:
        """
        Creates a set of options for running the Chrome browser.
        Runs Chrome in headless mode depending on the value of the RUN_HEADLESS environment variable.

        :return: A set of options to run the Chrome browser with.
        """
        chrome_options = webdriver.ChromeOptions()
        run_headless = should_run_headless()

        if run_headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-setuid-sandbox")

        return chrome_options
