from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://stellarburgers.education-services.ru/register')

driver.find_element(By.XPATH, ".//label[text()='Имя']/following-sibling::input").send_keys('Екатерина')
driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(f'katya_senko_35_{random.randint(100,999)}@yandex.ru')
driver.find_element(By.NAME, 'Пароль').send_keys('155')
driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

try:
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[text()='Некорректный пароль']")))
    print('PASSED')
except:
    print("FAILED")

driver.quit()
