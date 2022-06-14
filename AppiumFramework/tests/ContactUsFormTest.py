import time
import unittest
import pytest
from pages.ContactUsFormPage import ContactForm


# ap=AppiumService()
# ap.start()

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactUsFormTest(unittest.TestCase):

    # To Access this object through out the class we use pytest.fixture
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)

    @pytest.mark.run(order=1)
    def test_openContactForm(self):
        self.cf.clickContactFormButton()
#        self.cf.verifyContactPage()
    time.sleep(3)

    @pytest.mark.run(order=2)
    def test_enterFormData(self):
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMobileNo()

    @pytest.mark.run(order=3)
    def test_clickOnSubmitButton(self):
        self.cf.clickOnSubmitButton()


"""
#element = bp.waitForElement("com.code2lead.kwad:id/ContactUs", "id")
#element.click()
bp.screenshot("App")
element=bp.isDisplayed("com.code2lead.kwad:id/ContactUs", "id")
print(element)
bp.clickOnElement("com.code2lead.kwad:id/ContactUs", "id")
bp.sendText("TestName", "com.code2lead.kwad:id/Et2", "id")
bp.screenshot("TestName") """

""" cf.clickContactFormButton()
time.sleep(5)
cf.verifyContactPage()
cf.enterName()
cf.enterEmail()
cf.enterAddress()
cf.enterMobileNo()
cf.clickOnSubmitButton()"""

# ap.stop()
# driver.close()
