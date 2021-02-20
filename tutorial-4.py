# selenium tutorial 4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:/jxcky/bin/web-drivers/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=PATH, options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

actions = ActionChains(driver)
actions.click() # we can queue a bunch of actions then perform them
actions.perform()