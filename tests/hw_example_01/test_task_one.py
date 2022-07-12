from selenium.webdriver.common.by import By

from framework.common.driver import Driver
from framework.common.element import Element


class Elements:
    """
    All of the elements needed to complete task one.
    """

    def __init__(self, driver: Driver):
        self.driver = driver

    @property
    def frames(self) -> Element:
        return Element(driver=self.driver, locator=(By.XPATH, "//a[text()='Frames']"))

    @property
    def nested_frames(self) -> Element:
        return Element(driver=self.driver, locator=(By.XPATH, "//a[text()='Nested Frames']"))

    @property
    def first_body(self) -> Element:
        return Element(driver=self.driver, locator=(By.TAG_NAME, "body"))

    @property
    def first_div(self) -> Element:
        return Element(driver=self.driver, locator=(By.TAG_NAME, "div"))


def test_task_one(driver: Driver) -> None:
    """
    Task is defined as:

        Using Python and Selenium WebDriver, write a script to perform the following:
            1. Using Chrome,navigate directly to http://the-internet.herokuapp.com
            2. Follow the link titled Frames
            3. Follow the link to Nested Frames
            4. Print to the console the text in each frame in the following order:
                a. MIDDLE
                b. BOTTOM
                c. LEFT
                d. RIGHT
    """
    elements = Elements(driver=driver)

    elements.frames.wait_to_find().click()
    elements.nested_frames.wait_to_find().click()

    for frame in ["middle", "bottom", "left", "right"]:

        if frame == "bottom":
            driver.switch_to_frame(f"frame-{frame}")
            frame_text = elements.first_body.wait_to_find().text
        else:
            driver.switch_to_frame("frame-top")
            driver.switch_to_frame(f"frame-{frame}")

            if frame == "middle":
                frame_text = elements.first_div.wait_to_find().text
            else:
                frame_text = elements.first_body.wait_to_find().text

        print(frame_text)
        driver.switch_to_default_content()
