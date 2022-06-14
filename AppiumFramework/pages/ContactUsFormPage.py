from basepage.BasePage import BasePage
from Locators.ContactUsFromPageLocators import ContactUsFormLocators


class ContactForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickContactFormButton(self):
        self.clickOnElement(ContactUsFormLocators._contactFormButton, "id")

    #    def verifyContactPage(self):
    #        element = self.isDisplayed(self._pageTitle, "text")
    #        assert element == True

    def enterName(self):
        self.sendText("TestName", ContactUsFormLocators._enterName, "text")

    def enterEmail(self):
        self.sendText("text@yopmail.com", ContactUsFormLocators._enterEmail, "text")

    def enterAddress(self):
        self.sendText("123,address", ContactUsFormLocators._enterAddress, "text")

    def enterMobileNo(self):
        self.sendText("346584892", ContactUsFormLocators._enterMobileNo, "text")

    def clickOnSubmitButton(self):
        self.clickOnElement(ContactUsFormLocators._submitButton, "text")
