from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Login
from locators import Account
import urls
import data


class TestLogin:
    def assert_login(self, driver: webdriver.Chrome):
        driver.find_element(*Login.email_input_login).send_keys(data.EMAIL_OLD)
        driver.find_element(*Login.password_input_login).send_keys(data.PASSWORD)
        driver.find_element(*Login.login_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(urls.BASE_URL))
        driver.find_element(*Account.order_button)

    def test_login_to_account_from_main(self, driver: webdriver.Chrome):
        driver.get(urls.BASE_URL)
        driver.find_element(*Login.account_login).click()
        self.assert_login(driver)

    def test_login_from_personal_account(self, driver: webdriver.Chrome):
        driver.get(urls.BASE_URL)
        driver.find_element(*Login.personal_account).click()
        self.assert_login(driver)

    def test_login_from_registration(self, driver: webdriver.Chrome):
        driver.get(urls.BASE_URL+urls.REGISTER_PATH)
        driver.find_element(*Login.login_from_form).click()
        self.assert_login(driver)

    def test_login_from_forgot_password(self, driver: webdriver.Chrome):
        driver.get(urls.BASE_URL+urls.FORGOT_PASSWORD_PATH)
        driver.find_element(*Login.login_from_form).click()
        self.assert_login(driver)
