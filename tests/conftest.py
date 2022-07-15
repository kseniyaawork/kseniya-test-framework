import pytest

from framework.config.config import TestData
from framework.config.driver import Driver


@pytest.fixture(scope="class")
def init_driver(request):
    driver = Driver(url=TestData.BASE_URL)
    request.cls.driver = driver
    yield driver
    driver.close_and_quit()
