import unittest
from pages.ScrollViewPage import ScrollView
import pytest

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ScrollViewTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def clasObjects(self):
        self.sv = ScrollView(self.driver)

    @pytest.mark.run(order=1)
    def test_clickOnScrollView(self):
        self.sv.clickonscrollview()
        self.sv.verify_scrollviewtitle()
        self.sv.clickOnButton()
