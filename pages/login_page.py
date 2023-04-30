from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginPageLocators
from locators.base_page_locators import BasePageLocators

from base.base_page import Base


class Login_page(Base, LoginPageLocators, BasePageLocators):

    url = 'https://domkniginn.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Getters
    def get_cabinet_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cabinet)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_login)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_enter)))


    # Actions
    def click_cabinet_button(self):
        self.get_cabinet_button().click()
        print("Click cabinet button")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")


    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_cabinet_button()
        self.input_user_name("new_user")
        self.input_password("DomKnigi2023")
        self.click_login_button()
