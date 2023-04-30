import pytest
from pages.cart_page import CartPage
from pages.main_page import Main_page


@pytest.fixture()
def add_cart(driver):
    mp = Main_page(driver)
    mp.select_pelevin_product()
    yield

def test_delete_cart(driver, auth, add_cart):
    cp = CartPage(driver)
    cp.select_delete_product_1()

def test_delete_all_products_cart(driver, auth, add_cart):
    cp = CartPage(driver)
    cp.select_delete_all_products()