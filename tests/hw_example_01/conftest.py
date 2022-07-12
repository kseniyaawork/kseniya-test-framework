import os
import subprocess
from typing import Generator

import pytest

from framework.common.driver import Driver
from framework.common.env_vars import get_is_inside_wsl


@pytest.fixture(name="driver")
def start_chrome_webdriver() -> Generator:
    """
    Configures and starts the Selenium WebDriver to run the Chrome browser.

    :return: An instance of Driver.
    """
    if get_is_inside_wsl() in ["True", "true"]:
        os.environ["DISPLAY"] = _get_wsl_host_address()
    driver = Driver(url="http://the-internet.herokuapp.com/")
    yield driver
    driver.close_and_quit()


def _get_wsl_host_address() -> str:
    """
    :return: ip:port for wsl host
    """
    wsl_hostname_ip = subprocess.check_output("cat /etc/resolv.conf | grep nameserver | awk '{print $2}'", shell=True)
    return f"{wsl_hostname_ip.decode('utf-8').strip()}:0"
