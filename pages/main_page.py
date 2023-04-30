from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.constants import Constants
from base.base_page import Base
from locators.main_page_locators import MainPageLocators

url = "https://domkniginn.ru/"

class Main_page(Base, MainPageLocators, Constants):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters

    def get_pelevin_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pelevin_product)))

    def get_alyahov_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.alyahov_product)))

    def get_more_product_psycho(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_more_product)))

    def get_psychoanalys_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_psychoanalys)))

    def get_product_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))


    def get_product_name_text(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.cart_product_name)

    def get_product_price_text(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.cart_price)

    def get_total_cart_product_price(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.total_cart_price)


    # Переход на страницу продукта

    def click_select_pelevin_product(self):
        self.get_pelevin_product().click()
        print("Click select product 1")

    def click_select_alyahov_product(self):
        self.get_alyahov_product().click()
        print("Click select product 1")

    def click_select_psychoanalys_product(self):
        self.get_psychoanalys_product().click()

    def click_select_more_product_psycho(self):
        self.get_more_product_psycho().click()

    # Добавление в корзину

    def click_add_cart_product(self):
        self.get_product_to_cart().click()

    # Переход в корзину

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    # сравнение полей продукта

    def check_cart_product_name(self):
        return self.get_product_name_text().text

    def check_cart_product_price(self):
        return self.get_product_price_text().text

    # сравнение полей нескольких продуктов

    def check_total_product_price(self):
        return self.get_total_cart_product_price().text


    # Methods
    def get_url_not_auth(self):
        self.driver.get(url)
        self.driver.maximize_window()
        self.get_current_url()

    def select_pelevin_product(self):
        self.get_current_url()
        self.click_select_pelevin_product()
        self.click_add_cart_product()
        self.click_cart()
        self.assert_url("https://domkniginn.ru/site/cart")
        assert self.check_cart_product_name() == Constants.pelevin
        assert self.check_cart_product_price() == Constants.pelevin_price


    def select_alyahov_product(self):
        self.get_current_url()
        self.click_select_alyahov_product()
        self.click_add_cart_product()
        self.click_cart()
        self.assert_url("https://domkniginn.ru/site/cart")
        assert self.check_cart_product_name() == Constants.ilyahov
        assert self.check_cart_product_price() == Constants.ilyahov_price

    def select_psychoanalis_product(self):
        self.get_current_url()
        self.click_select_more_product_psycho()
        self.click_select_psychoanalys_product()
        self.click_add_cart_product()
        self.click_cart()
        self.assert_url("https://domkniginn.ru/site/cart")

    def select_various_products(self):
        self.get_current_url()
        self.click_select_pelevin_product()
        self.click_add_cart_product()
        self.driver.get(url)
        self.click_select_alyahov_product()
        self.click_add_cart_product()
        self.driver.get(url)
        self.click_select_more_product_psycho()
        self.click_select_psychoanalys_product()
        self.click_add_cart_product()
        self.click_cart()
        self.assert_url("https://domkniginn.ru/site/cart")
        assert self.check_total_product_price() == Constants.total_price
        # assert self.check_cart_product_price() == Constants.ilyahov_price

