from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL = "//input[@id='email']"
    PASSWORD = "//input[@id='passwd']"
    FORGOT_YOUR_PASS = (By.XPATH, "//a[@title='Recover your forgotten password']")
    SIGNIN_BUTTON = "//span[normalize-space()='Sign in']"
    EMAIL_FOR_REGESTRY = "//input[@id='email_create']"
    CREATE_ACCOUNT_BUTTON = "//span[normalize-space()='Create an account']"
