from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Login
from locators import Account
import urls
import data

class LoginTestHelper:
    @staticmethod
    def assert_login(driver: webdriver.Chrome):
        driver.find_element(*Login.email_input_login).send_keys(data.EMAIL_OLD)
        driver.find_element(*Login.password_input_login).send_keys(data.PASSWORD)
        driver.find_element(*Login.login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(urls.BASE_URL))
        driver.find_element(*Account.order_button)