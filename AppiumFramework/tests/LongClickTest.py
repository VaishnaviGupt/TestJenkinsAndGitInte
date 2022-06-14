import unittest
import pytest
from pages.LongClickPage import LongClick


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LongClickTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.lc = LongClick(self.driver)

    @pytest.mark.run(order=1)
    def test_performlongclick(self):
        self.lc.clickOnLongClick()
