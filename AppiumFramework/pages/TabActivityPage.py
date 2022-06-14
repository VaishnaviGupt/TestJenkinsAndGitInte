import time
from Locators.SwipeFromRightToLeft import SwipeLocators
from basepage.BasePage import BasePage
from appium.webdriver.common.touch_action import TouchAction


class TabActivityPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clickontabactivity(self):
        self.clickOnElement(SwipeLocators._tabactivity, "id")

    def swipefromhometosport(self):
        print("Device Width and Height : ", self.driver.get_window_size())
        # out of print statement is :Device Width and Height :  {'width': 1440, 'height': 2621}
        deviceSize = self.driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']

        ######Right to Left#######
        startx = screenWidth * 8 / 9
        endx = screenWidth / 9
        starty = screenHeight / 2
        endy = screenHeight / 2

        ###### Left to Right    #######
        startx2 = screenWidth / 9
        endx2 = screenWidth * 8 / 9
        starty2 = screenHeight / 2
        endy2 = screenHeight / 2

        actions = TouchAction(self.driver)
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        time.sleep(2)
        actions.long_press(None, startx2, starty2).move_to(None, endx2, endy2).release().perform()
