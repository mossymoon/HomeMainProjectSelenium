from pages.login_page import Login_page
from pages.main_page import Main_page

"""Выбор продукта с авторизацией"""
# выбор продукта из раздела Лидеры Продаж
def test_buy_pelevin_product(driver):
    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_pelevin_product()

# выбор продукта из раздела Бестселлеры
def test_buy_alyahov_product(driver):
    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_alyahov_product()

# выбор продукта через кнопку Посмотреть Все
def test_product_watch_all(driver):
    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_psychoanalis_product()

# выбор несколько продуктов в корзине
def test_various_products_add_cart(driver):
    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_various_products()


"""Выбор продукта без авторизации"""
# выбор продукта из раздела Лидеры Продаж
def test_buy_pelevin_product_not_auth(driver):
    mp = Main_page(driver)
    mp.get_url_not_auth()
    mp.select_pelevin_product()

# выбор продукта из раздела Бестселлеры
def test_buy_alyahov_product_not_auth(driver):
    mp = Main_page(driver)
    mp.get_url_not_auth()
    mp.select_alyahov_product()

# выбор продукта через кнопку Посмотреть Все
def test_product_watch_all_not_auth(driver):
    mp = Main_page(driver)
    mp.get_url_not_auth()
    mp.select_psychoanalis_product()

# выбор несколько продуктов в корзине
def test_various_products_add_cart_not_auth(driver):
    mp = Main_page(driver)
    mp.get_url_not_auth()
    mp.select_various_products()
