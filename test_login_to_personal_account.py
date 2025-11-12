from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://stellarburgers.education-services.ru')
driver.find_element(By.XPATH, './/header/nav/a').click()
time.sleep(3)

if "login" in driver.current_url:
    print("PASSED")
else:
    print("FAILED")

driver.quit()