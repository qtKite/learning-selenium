# selenium tutorial 1
# https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
from selenium import webdriver

PATH = "C:/jxcky/bin/web-drivers/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)
driver.quit()