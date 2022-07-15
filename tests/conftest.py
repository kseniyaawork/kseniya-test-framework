import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
# @pytest.fixture
def get_chrome_options():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-dev-shm-usage");
    options.add_argument("--disable-setuid-sandbox")
    return options


@pytest.fixture(scope="class")
# @pytest.fixture
def init_driver(request, get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    driver.quit()

