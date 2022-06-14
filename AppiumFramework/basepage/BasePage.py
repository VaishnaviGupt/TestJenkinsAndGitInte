import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
import utilities.CustomLogger as cl
from appium.webdriver.common.appiumby import AppiumBy


class BasePage:
    log = cl.customer_logger()

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorValue, locatorType):
        locatortype = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,
                                                                                    ElementNotSelectableException])

        if locatorType == "id":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ID, locatorValue))
            return element
        elif locatorType == "class":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorValue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                         'UISelector().description("%s")' % (locatorValue)))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                         'UISelector().index("%d")' % int(locatorValue)))
            return element
        elif locatorType == "text":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                         'text("%s")' % (locatorValue)))
            return element
        elif locatorType == "xpath":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.XPATH, '%s' % (locatorValue)))
            return element
        else:
            self.log.info("Locator value " + locatorValue + " not found")

        return element

    def getElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info("Element found with LocatorType " + locatorType + " with the locatorValue: " + locatorValue)
            assert True
        except:
            self.log.info(("Element not found with LocatorType " + locatorType + " and with the locatorValue: "
                           + locatorValue))
            assert False

    def clickOnElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info(
                "Click on Element with LocatorType " + locatorType + " with the locatorValue: " + locatorValue)
            assert True
        except:
            self.log.info(("Unable to Click on Element with LocatorType " + locatorType + " and with the locatorValue: "
                           + locatorValue))
            assert False

    def sendText(self, text, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Enter the Element with LocatorType " + locatorType + "with the locatorValue: " + locatorValue)
            assert True
        except:
            self.log.info(("Unable to Enter the Element with LocatorType " + locatorType + "and with the locatorValue: "
                           + locatorValue))
#           self.takeScreenshot(locatorType)
            assert False

    def isDisplayed(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info(
                "Click on Element with LocatorType " + locatorType + " with the locatorValue: " + locatorValue)
        except:
            self.log.info(("Unable to Click on Element with LocatorType " + locatorType + " and with the locatorValue: "
                           + locatorValue))

    def screenshot(self, screenshotName):
        fileName = screenshotName + " " + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDir = "../screenshots/"
        screenshotPath = screenshotDir + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path " + screenshotPath)
        except:
            self.log.info("Unable to save Screenshot to Path " + screenshotPath)


