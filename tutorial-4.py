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

# wait 5 seconds so page loads
driver.implicitly_wait(3)

cookieButton = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, 1)]

actions = ActionChains(driver)
actions.click(cookieButton) # we can queue a bunch of actions then perform them

for i in range(5000):
    actions.perform()
    count = cookie_count.text.split(" ")[0]
    print("cookies: " + count)

    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_action.perform()