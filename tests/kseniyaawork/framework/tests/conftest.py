import pytest
from selenium import webdriver


@pytest.fixture
def init_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield
    driver.close()







