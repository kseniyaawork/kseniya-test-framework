# Задача: написать тест для доступа к элементам сайта (нажать кнопку,
# ввести данные в форму)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture
def get_chrome_options():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument("--disable-setuid-sandbox")
    return options

@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
    return driver

def test_access_to_element(get_webdriver):
    driver = get_webdriver
    driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
    driver.implicitly_wait(5)

    driver.find_element(By.XPATH,
                                     "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[6]/div[2]/form[1]/div[1]/button[1]")

    driver.close()



def test_enter_data_into_form(get_webdriver):
    driver = get_webdriver
    driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
    driver.implicitly_wait(5)
    try:
        button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[6]/div[2]/form[1]/div[1]/button[1]")
        name = driver.find_element(By.ID, "et_pb_contact_name_0")
        email = driver.find_element(By.ID,"et_pb_contact_email_0")
        name.send_keys("test")
        assert "test" in name.get_attribute("value")
        email.send_keys("test@test.com")
        assert "test@test.com" in email.get_attribute("value")
        button.submit()
    finally:
        driver.close()


