import time

from appium import webdriver

class AndroidApp:

    userName = ""  #Enter your LT Username here
    accessKey = "" #Enter your LT AccessKey here
    gridURL = ""

    DeviceValue=""
    versionValue=""
    PlatformValue=""


   # @org.testng.annotations.Parameters(value = {"device", "version", "platform"})
    def AndroidApp(device, version, platform):
        try:
            DeviceValue = device;
            versionValue = version;
            PlatformValue = platform;
            desired_caps={}
            desired_caps["build"]="ParallelSample Android"
            desired_caps["deviceName"]=device
            desired_caps["platformVersion"]=version
            desired_caps["platformName"]=platform
            desired_caps["isRealMobile"]=True
            #AppURL (Create from Wikipedia.apk sample in project)
            desired_caps["app"]="" #Enter your app URL from previous step here
            desired_caps["deviceOrientation"]="PORTRAIT"
            desired_caps["console"]=True
            desired_caps["network"]=True
            desired_caps["visual"]=True
            desired_caps["devicelog"]=True

            hub = "https://" + AndroidApp.userName + ":" + AndroidApp.accessKey + AndroidApp.gridURL
            driver = webdriver.Remote(hub, desired_caps)

            color =driver.findElementById("com.lambdatest.proverbial:id/color")
            #Changes color
            color.click()
            #Back to black color
            color.click()

            text =driver.findElementById("com.lambdatest.proverbial:id/Text")
            #Changes the text to proverbial
            text.click()

            #toast is visible
            toast =driver.findElementById("com.lambdatest.proverbial:id/toast")
            toast.click()

            #notification is visible
            notification =driver.findElementById("com.lambdatest.proverbial:id/notification")
            notification.click()

            #Open the geolocation page
            geo =driver.findElementById("com.lambdatest.proverbial:id/geoLocation")
            geo.click()
            time.sleep(5000)

            #takes back to home page
            home = driver.findElementByAccessibilityId("Home")
            home.click()

            #Takes to speed test page
            speedtest =driver.findElementById("com.lambdatest.proverbial:id/speedTest")
            speedtest.click()
            time.sleep(5000)
            el10 = driver.findElementByXPath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View/android.widget.Button")
            el10.click()
            time.sleep(25000)


            el11 = driver.findElementByXPath("//android.widget.FrameLayout[@content-desc=\"Home\"]/android.widget.FrameLayout/android.widget.ImageView")
            el11.click()

            #Opens the browser
            browser = driver.find_element_by_accessibility_id("Browser")
            browser.click();
            el13 = driver.findElementById("com.lambdatest.proverbial:id/url")
            el13.send_keys("www.lambdatest.com")
            el14 = driver.findElementById("com.lambdatest.proverbial:id/find")
            el14.click()
            driver.quit()
        except:
            print("An Exception Occurs")

