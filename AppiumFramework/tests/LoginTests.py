import time

import pytest
import unittest

from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def clasObjects(self):
        self.lg = LoginPage(self.driver)

    @pytest.mark.run(order=1)
    def test_clickonlogin(self):
        self.lg.click_on_login()
        self.lg.verify_login_title()
    time.sleep(3)

    @pytest.mark.run(order=2)
    def test_enterloginform(self):
        self.lg.enter_email()
        self.lg.enter_password()
        self.lg.click_on_login_button()

    @pytest.mark.run(order=3)
    def test_verifyadmintitle(self):
        self.lg.verify_admin_title()

    @pytest.mark.run(order=4)
    def test_enteradminform(self):
        self.lg.enter_admin()
        self.lg.click_on_submit_button()
