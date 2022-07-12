from typing import Callable, List

from selenium.webdriver.common.by import By

from framework.common.driver import Driver
from framework.common.element import Element


class TableElement(Element):
    """
    An object that represents a table in the DOM tree.
    """

    def __init__(
        self,
        driver: Driver,
        xpath_locator: str,
        row_cells_locator: Callable[[str], str] = lambda text: f".//td[text()='{text}']/..//td",
    ) -> None:
        """
        :param driver: An instance of Dver.
        :param xpath_locator: The XPATH locator to find the table.
        :param row_cells_locator: A function to find all cells in a row that text matches the given text,
        e.g. lambda text: f"//td[text()='{text}']/../td"
        """
        super().__init__(driver, locator=(By.XPATH, xpath_locator))
        self._row_cells_locator = row_cells_locator
        self.column_names = [e.text for e in self.wait_to_find().get_child_elements((By.CSS_SELECTOR, "* th"))]

    def get_cell_by_first_row_value_and_column_name(self, first_row_value: str, column_name: str) -> Element:
        """
        Finds and returns the first cell that matches the given row and column values. For example:

        |ID    |First Name    |Last Name    |
        |1     |John          |Smith        |
        |2     |Jane          |Doe          |

        To get the cell containing John's first name, you would call this method using:
            cell = get_cell_by_first_row_value_and_column_name(first_row_value="John", column_name="First Name")
            assert cell.text == "John" # pass

        :param first_row_value: The row value to look for.
        :param column_name: The column name to look for (full match required).
        :return: The cell as an Element object.
        """
        row_cells: List[Element] = self.get_child_elements((By.XPATH, self._row_cells_locator(first_row_value)))
        return row_cells[self.column_names.index(column_name)]
