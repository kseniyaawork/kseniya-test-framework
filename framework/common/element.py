import time
from typing import List, Optional, TypeVar

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from framework.common.driver import Driver

ElementType = TypeVar("ElementType", bound="Element")


class Element:
    """
    An object that represents an element in the DOM tree.
    """

    def __init__(
        self: ElementType,
        driver: Driver,
        locator: tuple,
        web_element: Optional[WebElement] = None,
        timeout_s: int = 15,
    ) -> None:
        self._driver = driver
        self._web_driver = self._driver.driver
        self.locator = locator
        self.timeout_s = timeout_s
        self._search_from_root = WebDriverWait(self._web_driver, self.timeout_s)
        self._search_from_parent: Optional[WebDriverWait] = None
        self._web_element: Optional[WebElement] = web_element
        if self._web_element:
            self._init_parent_wait()

    @property
    def text(self) -> str:
        return self._web_element.text

    def click(self) -> None:
        """
        Clicks the element.
        """
        self._web_element.click()

    def get_child_elements(self, locator: tuple) -> List["Element"]:
        """
        Waits and returns child elements based on the given locator.

        :param locator: The locator to use to find child elements.
        :return: A list of child Elements.
        """
        children = self._search_from_parent.until(ec.presence_of_all_elements_located(locator))
        return [Element(driver=self._driver, locator=locator, web_element=e) for e in children]

    def highlight(self: ElementType, duration: float = 0.5) -> ElementType:
        """
        Highlights the element by changing its style to yellow background with red border for a provided time duration.
        After the duration has expired, the element's style will be restored to its original state.

        :param duration: The time (in seconds) to highlight the element.
        :return: The same instance of Element.
        """
        original_style = self._get_attribute("style")
        self._apply_style("background: yellow; border: 2px solid red;")
        time.sleep(duration)
        self._apply_style(original_style)
        return self

    def wait_to_disappear(self: ElementType) -> ElementType:
        """
        Polls to find an invisible element. This is an element with `display: none` style or not present in the DOM.
        If a matching WebElement is found, it hydrates the web_element field of this object.
        If no matching WebElement is found within the time limit, a TimeoutException is thrown.

        :return: The same instance of Element.
        """
        self._web_element = self._search_from_root.until(ec.invisibility_of_element_located(self.locator))
        self._init_parent_wait()
        return self

    def wait_to_find(self: ElementType) -> ElementType:
        """
        Polls to find the element using the locator defined when creating this object.
        If a matching WebElement is found, it hydrates the _web_element field of this object.
        If no matching WebElement is found within the time limit, a TimeoutException is thrown.

        :return: The same instance of Element.
        """
        self._web_element = self._search_from_root.until(ec.visibility_of_element_located(self.locator))
        self._init_parent_wait()
        return self

    def _apply_style(self, style: str) -> None:
        """
        Applies the provided style to the element.

        :param style: The style to apply to the element. This should be in the format of `key: value` pair and
        separated by semicolon (e.g. "background: yellow; border: 2px solid red;").
        """
        self._web_driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", self._web_element, style)

    def _get_attribute(self, attribute: str) -> str:
        """
        Get an attribute of the element with the given name.

        :param attribute: The attribute.
        """
        return self._web_element.get_attribute(attribute)

    def _init_parent_wait(self) -> None:
        """
        Initializes a wait with the current Element instance, allowing to wait to find child elements.
        Should only be called after self._web_element has been defined
        """
        self._search_from_parent = WebDriverWait(self._web_element, self.timeout_s)
