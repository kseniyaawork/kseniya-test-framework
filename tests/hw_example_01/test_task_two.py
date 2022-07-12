from selenium.webdriver.common.by import By

from framework.common.driver import Driver
from framework.common.element import Element


class Elements:
    """
    All of the elements needed to complete task two.
    """

    def __init__(self, driver: Driver):
        self.driver = driver

    @property
    def start(self) -> Element:
        return Element(driver=self.driver, locator=(By.XPATH, "//div[@id='start']//button[text()='Start']"))

    @property
    def loading(self) -> Element:
        return Element(driver=self.driver, locator=(By.XPATH, "//div[@id='loading']"))

    @property
    def finished(self) -> Element:
        return Element(driver=self.driver, locator=(By.XPATH, "//div[@id='finish']//h4"))


def test_task_two(driver: Driver) -> None:
    """
    Task is defined as:

        Using Python and Selenium WebDriver, write a script to perform the following:
            1. Using Chrome,navigate directly to http://the-internet.herokuapp.com/dynamic_loading/1
            2. Click Start
            3. When the loading animation has finished, print the text that is displayed to the console
    """
    driver.go_to_url("http://the-internet.herokuapp.com/dynamic_loading/1")
    elements = Elements(driver=driver)

    elements.start.wait_to_find().click()
    elements.loading.wait_to_find().wait_to_disappear()
    text = elements.finished.wait_to_find().text
    print(text)
