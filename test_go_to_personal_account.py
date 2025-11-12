from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://stellarburgers.education-services.ru/login')
driver.find_element(By.NAME, 'name').send_keys('katya_senko_35_195@yandex.ru')
driver.find_element(By.NAME, 'Пароль').send_keys('katya55')
driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
time.sleep(3)

if driver.current_url == 'https://stellarburgers.education-services.ru':
    url_before_click = driver.current_url
    driver.find_element(By.XPATH, './/header/nav/a').click()
    if driver.current_url != url_before_click:
        print("PASSED")
    else:
        print("FAILED")
else:
    print('FAILED')

driver.quit()