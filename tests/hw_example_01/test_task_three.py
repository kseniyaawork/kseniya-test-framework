from selenium.webdriver.common.by import By

from framework.common.driver import Driver
from framework.common.element import Element
from framework.common.element_table import TableElement


class Elements:
    """
    All of the elements needed to complete task three.
    """

    def __init__(self, driver: Driver):
        self.driver = driver

    @property
    def table(self) -> TableElement:
        return TableElement(driver=self.driver, xpath_locator="//div[@class='large-10 columns']//table")

    @property
    def qux(self) -> Element:
        return Element(driver=self.driver, locator=(By.CSS_SELECTOR, ".success"))


def test_task_three(driver: Driver) -> None:
    """
    Task is defined as:

        Using Python and Selenium WebDriver, write a script to perform the following in sequence:
            1. Using Chrome, navigate directly to http://the-internet.herokuapp.com/challenging_dom
            2. Highlight the text in the third row of the Diceret column for two seconds
            3. Highlight the delete link in the row containing Apeirian7 for two seconds
            4. Highlight the edit link for the row containing Apeirian2 for two seconds
            5. Highlight Definiebas7 for two seconds, then highlight Luvaret7 for two seconds
            6. Click the quxbutton

        This is to test how you traverse tables, not just how you locate text elements,so please consider this in
        your solution.
    """
    driver.go_to_url("http://the-internet.herokuapp.com/challenging_dom")
    elements = Elements(driver=driver)

    table = elements.table.wait_to_find()
    duration = 2
    cells = {
        "Phaedrum2": "Diceret",
        "Apeirian7": "Action",
        "Apeirian2": "Action",
        "Definiebas7": "Sit",
        "Iuvaret7": "Lorem",
    }
    for row, column in cells.items():
        table.get_cell_by_first_row_value_and_column_name(first_row_value=row, column_name=column).highlight(
            duration=duration
        )

    elements.qux.wait_to_find().click()
