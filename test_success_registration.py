from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://stellarburgers.education-services.ru/register')

driver.find_element(By.XPATH, ".//label[text()='Имя']/following-sibling::input").send_keys('Екатерина')
driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(f'katya_senko_35_{random.randint(100,999)}@yandex.ru')
driver.find_element(By.NAME, 'Пароль').send_keys(f'katya{random.randint(10,99)}')
driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
time.sleep(3)

if "login" in driver.current_url:
    print("PASSED")
else:
    print("FAILED")

driver.quit()