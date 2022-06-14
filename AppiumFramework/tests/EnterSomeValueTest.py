import time
import unittest
import pytest
from pages.EnterSomeValuePage import EnterSomeValue


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class EnterValueTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.ev = EnterSomeValue(self.driver)

    @pytest.mark.run(order=1)
    def test_openEnterSomeValuePage(self):
        self.ev.clickentersomevaluebutton()
#        self.ev.verifyEnterSomeValueTitle()

    @pytest.mark.run(order=2)
    def test_enterSomeValue(self):
        self.ev.entersomevaluetext()

    @pytest.mark.run(order=3)
    def test_clickOnSubmitButton(self):
        self.ev.clickonsubmitbutton()


