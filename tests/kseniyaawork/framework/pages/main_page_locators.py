"""
В нем создайте новый класс MainPageLocators
Опишите локатор: LOCATOR_SING_IN_BUTTON = (By.CLASS_NAME, "login")
Импортируйте где надо новый класс с локатором и используйте его
следующим образом: *MainPageLocators.LOCATOR_SING_IN_BUTTON
"""
from selenium.webdriver.common.by import By

class MainPageLocators:
    def locator_sign_in_button:
        locator_sign_in_button = (By.CLASS_NAME, "button btn btn-default button-medium")