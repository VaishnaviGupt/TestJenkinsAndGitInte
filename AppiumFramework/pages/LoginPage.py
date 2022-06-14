from Locators.LoginPageLocators import LoginPageLocators
from basepage.BasePage import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_login(self):
        self.clickOnElement(LoginPageLocators._login, "id")

    def verify_login_title(self):
        self.isDisplayed(LoginPageLocators._LoginPageTitle, "text")

    def enter_email(self):
        self.sendText("admin@gmail.com", LoginPageLocators._enterEmail, "text")

    def enter_password(self):
        self.sendText("admin123", LoginPageLocators._enterPassword, "text")

    def click_on_login_button(self):
        self.clickOnElement(LoginPageLocators._loginButton, "text")

    def verify_admin_title(self):
        self.isDisplayed(LoginPageLocators._admintitle, "text")

    def enter_admin(self):
        self.sendText("admin", LoginPageLocators._enteradmin, "id")

    def click_on_submit_button(self):
        self.clickOnElement(LoginPageLocators._submitbutton, "text")
