from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait as wait1
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                "deviceName": "IPhone X",
                "platformName": "iOS",
                "platformVersion": "11.1",
                "automationName": "Appium",
                "xcodeOrgId": "FRGCAGTTW9",
                "app": "/Users/rahul/Desktop/MyKaarma.app",
                "xcodeSigningId": "iPhone Developer",
                "autoAcceptAlerts": "true",
                "udid": "6C17C181-0A4D-40DC-8AC0-15124CF9FE43"})

e1 = wait1(driver, 30).until(EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID, 'hamburger menu')))
e1.click()
e2 = wait1(driver, 30).until(EC.visibility_of_element_located((MobileBy.IOS_PREDICATE, "type == 'XCUIElementTypeStaticText' AND value BEGINSWITH[c] 'Video WalkAround' AND visible == 1")))
e2.click()
wait1(driver, 30).until(EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID, "inspectionMainView_mileageField")))
driver.find_element_by_accessibility_id('inspectionMainView_mileageField').send_keys("2000")
driver.find_element_by_accessibility_id('inspectionMainView_hangtagField').send_keys("test_tag")
driver.find_element_by_accessibility_id('Return').click()
driver.find_element_by_accessibility_id('inspectionMainView_noVinBtn').click()
wait1(driver, 30).until(EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID, "Search Customer")))
driver.find_element_by_accessibility_id('Search Customer').send_keys("Rahul Testman")



username = wait1(driver, 30).until(EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID, 'tbUsername')))
username.send_keys("rishi-prod")
driver.find_element_by_accessibility_id('bSignIn').click()
e1 = wait1(driver, 30).until(EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID, 'hamburger menu')))
e1.click()
e2 = wait1(driver, 30).until(EC.visibility_of_element_located((MobileBy.IOS_PREDICATE, "type == 'XCUIElementTypeStaticText' AND value BEGINSWITH[c] 'Video WalkAround' AND visible == 1")))
e2.click()
wait1(driver, 30).until(EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID, "inspectionMainView_mileageField")))
driver.find_element_by_accessibility_id('inspectionMainView_mileageField').send_keys("2000")
driver.find_element_by_accessibility_id('inspec790020tionMainView_hangtagField').send_keys("test_tag")
driver.find_element_by_accessibility_id('Return').click()
driver.find_element_by_accessibility_id('inspectionMainView_noVinBtn').click()
wait1(driver, 30).until(EC.visibility_of_element_located((MobileBy.ACCESSIBILITY_ID, "Search Customer")))
driver.find_element_by_accessibility_id('Search Customer').send_keys("Rahul Testman")

