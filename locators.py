from selenium import webdriver
from selenium.webdriver.common.by import By

class Constructor:
    sauses_tab = (By.XPATH, ".//span[text()='Соусы']")  #Вкладка Соусы
    fillings_tab = (By.XPATH, ".//span[text()='Начинки']")  #Вкладка Начинки
    buns_tab = (By.XPATH, ".//span[text()='Булки']")  #Вкладка Булки
    active_tab = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]/span") #Активный таб

class Registration:
    name_input = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")  #Поле Имя в форме регистрации
    email_input = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  #Поле Имейил в форме регистрации
    password_input = (By.NAME, 'Пароль')  #Поле Пароль в форме регистрации
    signup_button = (By.XPATH, "//button[text()='Зарегистрироваться']")  #кнопка Зарегистрировать в поле регистрации
    password_error = (By.CLASS_NAME, "input__error")
    
class Login:
    account_login = (By.XPATH, ".//button[text()='Войти в аккаунт']")  #Кнопка Войти в аккаунт на главной странице
    personal_account = (By.XPATH, ".//header/nav/a[@href='/account']")  #Личный кабинет на главной странице
    login_from_form = (By.XPATH, ".//main/div/div/p/a[@href='/login']")  #Ссылка Войти под формой регистрации
    login_forgot_password = (By.XPATH, ".//main/div/div/p/a[@href='/forgot-password']")  #Ссылка Восстановить пароль на странице входа в аккаунт
    email_input_login = (By.NAME, 'name') #Поле Имейл во входе
    password_input_login = (By.NAME, 'Пароль') #Поле пароль во входе
    login_button = (By.XPATH, ".//button[text()='Войти']")  #Кнопка Войти на странице входа в аккаунт

class Account:
    constructor = (By.XPATH, ".//header/nav/ul/li/a[@href='/']") #Кнопка Конструктор на главной страницу
    logo = (By.XPATH, ".//header/nav/div/a[@href='/']") #Логотип на главной странице
    logout_button = (By.XPATH, ".//button[text()='Выход']") #Кнопка Выход из личного кабинета
    order_button = (By.XPATH, ".//button[text()='Оформить заказ']")  #Кнопка оформить заказ на главной странице