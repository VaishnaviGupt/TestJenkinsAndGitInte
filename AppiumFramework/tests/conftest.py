import time
import pytest
import utilities.CustomLogger as cl
from basepage.BasePage import BasePage
from basepage.DriverClass import Driver


@pytest.fixture(scope='class')
def beforeClass(request):
    print("Before class")
    log = cl.customer_logger()
    log.info("Launch App")
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:  # We are changing the scope of using driver to Class
        request.cls.driver = driver
    yield
    time.sleep(5)
    driver.quit()
    print("After a class")


@pytest.fixture()
def beforeMethod():
    print("Before a method")
    yield
    print("After a method")
