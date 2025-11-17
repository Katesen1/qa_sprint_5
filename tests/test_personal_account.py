from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Login
from locators import Account
import urls

class TestPersonalAccount:
    def test_go_to_personal_account_autorized(self, driver: webdriver.Chrome, login):
        driver.get(urls.BASE_URL)
        driver.find_element(*Login.personal_account).click()
        assert urls.BASE_URL + urls.ACCOUNT_PROFILE_PATH == driver.current_url
        
    def test_to_constructor_from_account(self, driver: webdriver.Chrome, login):
        driver.get(urls.BASE_URL + urls.ACCOUNT_PATH)
        driver.find_element(*Account.constructor).click()
        assert urls.BASE_URL == driver.current_url

    def test_to_logo(self, driver: webdriver.Chrome, login):
        driver.get(urls.BASE_URL + urls.ACCOUNT_PATH)
        driver.find_element(*Account.logo).click()
        assert urls.BASE_URL == driver.current_url
    
    def test_logout(self, driver: webdriver.Chrome, login):
        driver.get(urls.BASE_URL + urls.ACCOUNT_PATH)
        account_url = driver.current_url
        driver.find_element(*Account.logout_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_changes(account_url))
        assert urls.BASE_URL + urls.LOGIN_PATH == driver.current_url