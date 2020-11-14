from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
options = Options()
options.set_headless(headless=False)
options.binary = binary
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True #optional
driver = webdriver.Firefox(options=options, capabilities=cap, executable_path=r"C:\python\geckodriver-v0.23.0-win64\geckodriver.exe")
driver.get("http://google.com/")
print ("Headless Firefox Initialized")
driver.quit()