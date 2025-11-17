import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Login
import data
import urls

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login(driver:webdriver.Chrome):
    driver.get(urls.BASE_URL+urls.LOGIN_PATH)
    driver.find_element(*Login.email_input_login).send_keys(data.EMAIL_OLD)
    driver.find_element(*Login.password_input_login).send_keys(data.PASSWORD)
    driver.find_element(*Login.login_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be(urls.BASE_URL))