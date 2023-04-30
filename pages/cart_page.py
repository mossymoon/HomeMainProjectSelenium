import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.constants import Constants
from base.base_page import Base
from locators.cart_page_locators import CartPageLocators


class CartPage(Base, CartPageLocators, Constants):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Getters

    def get_delete_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_product_1)))

    def get_delete_all_products(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_all_products)))

    def get_empty_cart(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.XPATH, self.cart_is_empty)



    # удаление одного продукта из корзины

    def click_delete_product_1(self):
        self.get_delete_product_1().click()
        print("Click delete product 1")

    def allert_window_ok(self):
        try:
            confirm = self.driver.switch_to.alert
            confirm.accept()
            print("alert accepted")
        except:
            print("no alert")

    def check_empty_cart(self):
        return self.get_empty_cart().text



    # Methods

    def select_delete_product_1(self):
        self.click_delete_product_1()
        self.allert_window_ok()
        self.assert_url("https://domkniginn.ru/site/cart")
        assert self.check_empty_cart() == Constants.empty_cart

    def select_delete_all_products(self):
        self.get_delete_all_products().click()

