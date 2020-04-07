from selenium import webdriver

''' Chrome web driver interface
'''
hyperlink = "http://lambdatest.com"


driver = webdriver.Chrome(executable_path='/Users/rahul/IdeaProjects/myPro/src/test/resources/drivers/chromedriver')
driver.get(hyperlink)

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

''' Calculate the performance'''
backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart

print("Back End: %s" % backendPerformance_calc)
print("Front End: %s" % frontendPerformance_calc)

driver.quit()