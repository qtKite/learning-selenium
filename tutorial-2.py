# selenium tutorial 2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:/jxcky/bin/web-drivers/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=PATH, options=options)
driver.get("https://techwithtim.net")
search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(webdriver.common.keys.Keys.RETURN)
webdriver.remote.webelement.WebElement
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-header")
        print(type(header))
finally:
    driver.quit()

