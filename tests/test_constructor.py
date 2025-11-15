from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from locators import Constructor
import urls

class TestConstructor:
    def test_sauses(self, driver: webdriver.Chrome):
        driver.get(urls.BASE_URL)
        sauses = driver.find_element(*Constructor.sauses_tab)
        sauses.click()
        active = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((Constructor.active_tab)))
        assert 'Соусы' in active.text, "Таб 'Соусы' не активирован"

    def test_fillings(self, driver: webdriver.Chrome):
        driver.get(urls.BASE_URL)
        fillings = driver.find_element(*Constructor.fillings_tab)
        fillings.click()
        active = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((Constructor.active_tab)))
        assert 'Начинки' in active.text, "Таб 'Начинки' не активирован"

    def test_buns(self, driver: webdriver.Chrome):
        driver.get(urls.BASE_URL)
        sauses = driver.find_element(*Constructor.sauses_tab)
        sauses.click()
        buns = driver.find_element(*Constructor.buns_tab)
        buns.click()
        active = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((Constructor.active_tab)))
        assert 'Булки' in active.text, "Таб 'Булки' не активирован"