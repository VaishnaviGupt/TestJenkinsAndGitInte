import unittest

import pytest
from pages.TabActivityPage import TabActivityPage


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TabViewTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def clasObject(self):
        self.tv = TabActivityPage(self.driver)

    @pytest.mark.run(order=1)
    def test_tabviewswipe(self):
        self.tv.clickontabactivity()
