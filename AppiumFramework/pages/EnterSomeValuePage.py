from Locators.EnterSomeValuePageLocators import EnterSomeValueLocators
from basepage.BasePage import BasePage

class EnterSomeValue(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickentersomevaluebutton(self):
        self.clickOnElement(EnterSomeValueLocators._enterSomeValue, "id")

    #    def verifyEnterSomeValueTitle(self):
    #        element = self.isDisplayed(self._enterSomeValueTitle, "text")
    #       assert element == True

    def entersomevaluetext(self):
        self.sendText("TestValue", EnterSomeValueLocators._enterSomeValueText, "xpath")

    def clickonsubmitbutton(self):
        self.clickOnElement(EnterSomeValueLocators._submitButton, "text")
