from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://stellarburgers.education-services.ru')

try:
    sauses = driver.find_element(By.XPATH, ".//span[text()='Соусы']")
    sauses.click()
    sauses_section = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Соусы']")))
    driver.execute_script("arguments[0].scrollIntoView();", sauses_section) 
    print('PASSED')

    fillings = driver.find_element(By.XPATH, ".//span[text()='Начинки']")
    fillings.click()
    fillings_section = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,".//h2[text()='Начинки']")))
    driver.execute_script("arguments[0].scrollIntoView();", fillings_section) 
    print('PASSED')

    buns = driver.find_element(By.XPATH, ".//span[text()='Булки']")
    buns.click()
    buns_section = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,".//h2[text()='Булки']")))
    driver.execute_script("arguments[0].scrollIntoView();", buns_section) 
    print('PASSED')
except:
    print('FAILED')

driver.quit()