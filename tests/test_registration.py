from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Registration
import urls
import data

class TestRegistration:
    def test_success(self, driver: webdriver.Chrome):
        driver.get(urls.BASE_URL+urls.REGISTER_PATH)
        register_url = driver.current_url
        driver.find_element(*Registration.name_input).send_keys(data.USER_NAME)
        driver.find_element(*Registration.email_input).send_keys(data.EMAIL_NEW)
        driver.find_element(*Registration.password_input).send_keys(data.PASSWORD)
        driver.find_element(*Registration.signup_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_changes(register_url))
        assert urls.BASE_URL+urls.LOGIN_PATH == driver.current_url
        

    def test_invalid_password(self, driver: webdriver.Chrome):
        driver.get(urls.BASE_URL+urls.REGISTER_PATH)
        driver.find_element(*Registration.name_input).send_keys(data.USER_NAME)
        driver.find_element(*Registration.email_input).send_keys(data.EMAIL_NEW)
        driver.find_element(*Registration.password_input).send_keys(data.WRONG_PASSWORD)
        driver.find_element(*Registration.signup_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Registration.password_error))
        password_error = driver.find_element(*Registration.password_error)
        assert 'Некорректный пароль' in password_error.text

