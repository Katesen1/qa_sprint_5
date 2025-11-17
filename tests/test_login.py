from selenium import webdriver
from locators import Login
import urls
from heplers import LoginTestHelper

class TestLogin:

    def test_login_to_account_from_main(self, driver: webdriver.Chrome):
        driver.get(urls.BASE_URL)
        driver.find_element(*Login.account_login).click()
        LoginTestHelper.assert_login(driver)

    def test_login_from_personal_account(self, driver: webdriver.Chrome):
        driver.get(urls.BASE_URL)
        driver.find_element(*Login.personal_account).click()
        LoginTestHelper.assert_login(driver)

    def test_login_from_registration(self, driver: webdriver.Chrome):
        driver.get(urls.BASE_URL+urls.REGISTER_PATH)
        driver.find_element(*Login.login_from_form).click()
        LoginTestHelper.assert_login(driver)

    def test_login_from_forgot_password(self, driver: webdriver.Chrome):
        driver.get(urls.BASE_URL+urls.FORGOT_PASSWORD_PATH)
        driver.find_element(*Login.login_forgot_password).click()
        LoginTestHelper.assert_login(driver)
