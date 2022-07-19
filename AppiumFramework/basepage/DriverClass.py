from appium import webdriver


class Driver():

    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '12'
        desired_caps['deviceName'] = 'Pixel 2 API 32'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['app'] = ('/Users/goldi.garg/Downloads/Android_Demo_App.apk')
        # desired_caps['appPackage']=''
        # desired_caps['appActivity']=''

        driver = webdriver.Remote("", desired_caps)

        return driver
