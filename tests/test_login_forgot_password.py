from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://stellarburgers.education-services.ru/login')
driver.find_element(By.XPATH, ".//main/div/div/p/a[@href='/forgot-password']").click()
time.sleep(3)

if "forgot-password" in driver.current_url:
    print("PASSED")
else:
    print("FAILED")

driver.quit()