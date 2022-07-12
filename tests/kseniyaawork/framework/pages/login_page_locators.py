from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

# driver = webdriver.Chrome()


class LoginPageLocators:
    driver = webdriver.Chrome()
    driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
    EMAIL = driver.find_element(By.XPATH, "//input[@id='email']")
    PASSWORD = driver.find_element(By.XPATH, "//input[@id='passwd']")
    FORGOT_YOUR_PASS = (By.XPATH, "//a[@title='Recover your forgotten password']")
    SIGNIN_BUTTON = driver.find_element(By.XPATH, "//span[normalize-space()='Sign in']")


# driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
# flag = driver.find_element(By.XPATH, "//input[@id='email']")
# assert flag


