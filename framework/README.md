# To run the tests

### Via PyCharm
- Confirm that PyCharm has been configured correctly: project interpreter and environment variables
- Navigate to any of the `tests/test_*` files and use the PyCharm UI to run the test
It should pass first time.

### Via CLI

To run all the tasks, it's advisable to do that via the command line. This can be done via the following command
from the `kseniya-test-framework` folder:

```shell
poetry shell
poetry run python -m pytest framework/tests/
```

### Via Docker

To run the tests inside a container using the image [built here](../README.md#docker):

```shell
docker run aut:local /bin/bash -c "poetry run python -m pytest framework/tests/"
```
### Expected successful pytest report
```
================================================= test session starts ==================================================
platform linux -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /home/kseniyaawork/kseniya-test-framework/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/kseniyaawork/kseniya-test-framework, configfile: pytest.ini
plugins: allure-pytest-2.9.45
collected 5 items

framework/tests/test_login_page.py::TestLoginPage::test_open_login_page PASSED                                   [ 20%]
framework/tests/test_login_page.py::TestLoginPage::test_login_page_title PASSED                                  [ 40%]
framework/tests/test_login_page.py::TestLoginPage::test_forgot_your_pass_link_visible PASSED                     [ 60%]
framework/tests/test_login_page.py::TestLoginPage::test_login PASSED                                             [ 80%]
framework/tests/test_login_page.py::TestLoginPage::test_register PASSED                                          [100%]

================================================== 5 passed in 8.00s =================================================
```
