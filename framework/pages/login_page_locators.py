from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL = (By.XPATH, "//input[@id='email']")
    PASSWORD = (By.XPATH, "//input[@id='passwd']")
    FORGOT_YOUR_PASS = (By.XPATH, "//a[@title='Recover your forgotten password']")
    SIGNIN_BUTTON = (By.XPATH, "//span[normalize-space()='Sign in']")
    EMAIL_FOR_REGESTRY = (By.XPATH, "//input[@id='email_create']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//span[normalize-space()='Create an account']")






