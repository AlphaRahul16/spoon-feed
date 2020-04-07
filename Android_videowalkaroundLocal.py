from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait as wait1
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import unittest
import time

class Android_videowalkaround(unittest.TestCase):

    def setUp(self):

        desired_capabilities = {
            "deviceName": "emulator-5554",
            "platformName": "Android",
            "platformVersion": "7.1.1",
            "automationName": "Appium",
            "app": "/Users/rahul/Downloads/myKaarma DirectConnect_v1.34.0_apkpure.com.apk",
            "appPackage": "com.mykaarma.android",
            "appActivity": "com.mykaarma.android.SplashScreenActivity",
            "deviceOrientation": "portrait",
            "autoGrantPermissions": "true",
            "autoAcceptAlerts": "true"}

        self.driver = webdriver.Remote(
            'http://127.0.0.1:4723/wd/hub', desired_capabilities)
        self.driver.implicitly_wait(10)


    def test_webview(self):
        time.sleep(5)
        username = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("tbUsername")')
        username.send_keys("rishi-prod")
        element = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("bSignIn")')
        element.click()
        password = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("password")')
        password.send_keys('P@55w0rd')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("bSignIn")').click()
        menu = wait1(self.driver, 30).until(EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Open navigation drawer')))
        menu.click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Video WalkAround")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.mykaarma.android:id/mileage")').send_keys('1000')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.mykaarma.android:id/hangTag")').send_keys('testTag')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.mykaarma.android:id/skipVinBtn")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("android:id/button1")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("android:id/search_src_text")').send_keys('raj@testing.com')
        time.sleep(3)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.mykaarma.android:id/customerSearchTextView")').click()
        self.driver.find_element_by_xpath('(//android.widget.TextView[@resource-id="com.mykaarma.android:id/vehicleDetail"])[1]').click()
        time.sleep(5)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.mykaarma.android:id/video")').click()
        time.sleep(5)
        action = TouchAction(self.driver)
        window_size = self.driver.get_window_size()
        xpoint = (window_size["width"] - 1/2)+50
        ypoint = (window_size["height"] - 1)/2
        count = 10
        while count < 0:
            action.tap(None, xpoint, ypoint, 1).perform()
            count = count - 1;
            time.sleep(2)
        print("complete")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.mykaarma.android:id/video")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.mykaarma.android:id/pendingInspectionsBtn")').click()
        walkaroundlabel = wait1(self.driver, 30).until(EC.visibility_of_element_located((MobileBy.ID, 'com.mykaarma.android:id/pastWalkaroundsLabel')))
        walkaroundlabel.is_displayed()
        self.driver.find_element_by_xpath('(//android.widget.TextView[@resource-id="com.mykaarma.android:id/currentlyUploadingLabelParent"])[1]').click()






    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_videowalkaround)
    unittest.TextTestRunner(verbosity=1).run(suite)

