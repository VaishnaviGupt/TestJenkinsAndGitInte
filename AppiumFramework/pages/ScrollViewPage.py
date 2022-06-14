from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait

from Locators.ScrollViewLocators import ScrollViewLocators
from basepage.BasePage import BasePage


class ScrollView(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickonscrollview(self):
        self.clickOnElement(ScrollViewLocators._scroll_view, "id")

    def verify_scrollviewtitle(self):
        self.isDisplayed(ScrollViewLocators._scroll_view_title, "text")

    def clickOnButton(self):
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,
                                                                                    ElementNotSelectableException])
        element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                      'new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON12"))'))
        element.click()
