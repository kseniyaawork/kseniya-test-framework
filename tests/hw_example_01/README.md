# Running Tests

### Via PyCharm
- Confirm that PyCharm has been configured correctly: project interpreter and environment variables
- Navigate to any of the `test_task_<number>` files and use the PyCharm UI to run the test
It should pass first time.

### Via CLI

To run all the tasks, it's advisable to do that via the command line. This can be done via the following command
from the `selenium-webdriver` folder:

```shell
export RUN_HEADLESS=False
export AUT_IS_INSIDE_WSL=True # if running inside WSL
poetry run python -m pytest
```

### Via Docker

To run the tests inside a container using the image [built here](../../README.md#docker):

```shell
docker run --env AUT_IS_INSIDE_WSL=False \
           --env RUN_HEADLESS=True \
           aut:local \
           /bin/bash -c "poetry run python -m pytest"
```
### Expected successful pytest report
```
=================================================================================== test session starts ====================================================================================
platform linux -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /home/klapshin/code/tms-ui-framework/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/klapshin/code/tms-ui-framework, configfile: pytest.ini
plugins: allure-pytest-2.9.45
collected 3 items

tests/01_hw_example/test_task_one.py::test_task_one PASSED                                                                                                                           [ 33%]
tests/01_hw_example/test_task_three.py::test_task_three PASSED                                                                                                                       [ 66%]
tests/01_hw_example/test_task_two.py::test_task_two PASSED                                                                                                                           [100%]

=============================================================================== 3 passed in 69.26s (0:01:09) ===============================================================================
```
