import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait

from Locators.LongClickLocators import LongClickLocators
from basepage.BasePage import BasePage


class LongClick(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickOnLongClick(self):
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,
                                                                                    ElementNotSelectableException])
        element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                      'new UiScrollable(new UiSelector()).scrollIntoView(text("LONG CLICK"))'))
        time.sleep(2)
        action=TouchAction(self.driver)
        action.long_press(element, 5)
        action.perform()