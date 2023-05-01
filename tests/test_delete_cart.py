import pytest
from pages.cart_page import CartPage
from pages.main_page import Main_page
from pages.finish_page import Finish_page

url = "https://domkniginn.ru/"

@pytest.fixture()
def add_cart(driver):
    mp = Main_page(driver)
    mp.select_pelevin_product()
    yield

@pytest.fixture()
def get_url_not_auth_del(driver):
    mp = Main_page(driver)
    mp.driver.get(url)
    mp.driver.maximize_window()
    mp.get_current_url()
    yield


"""Удаление продуктов в корзине для авторизованного"""
@pytest.mark.last
def test_delete_cart(driver, auth, add_cart):
    cp = CartPage(driver)
    cp.select_delete_product_1()
    f = Finish_page(driver)
    f.finish()
    print("last auth test 1")

@pytest.mark.last
def test_delete_all_products_cart(driver, auth, add_cart):
    cp = CartPage(driver)
    cp.select_delete_all_products()
    f = Finish_page(driver)
    f.finish()
    print("last auth test 2")

"""Удаление продуктов в корзине для неавторизованного"""
@pytest.mark.last
def test_delete_cart_not_auth(driver, get_url_not_auth_del, add_cart):
    cp = CartPage(driver)
    cp.select_delete_product_1()
    f = Finish_page(driver)
    f.finish()
    print("last not auth test 1")

@pytest.mark.last
def test_delete_all_products_cart_not_auth(driver, get_url_not_auth_del, add_cart):
    cp = CartPage(driver)
    cp.select_delete_all_products()
    f = Finish_page(driver)
    f.finish()
    print("last not auth test 2")