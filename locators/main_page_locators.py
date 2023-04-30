# локаторы для main page


class MainPageLocators:

    pelevin_product = "//a[@href='/goods/item/240947'][contains(text(), 'Empire V')]"
    alyahov_product = "//a[@href='/goods/item/543836'][contains(text(), 'Ясно, понятно: ')]"
    select_more_product = "//a[@href='/site/catalog/2379'][contains(text(), 'Посмотреть все')]"
    select_psychoanalys = "//a[@href='/goods/item/536626'][contains(text(), 'Психоанализ')]"
    cart_product_name = "//*[@id='order-table']/tbody/tr/td[1]"
    cart_price = "//*[@id='order-table']/tbody/tr/td[3]/span"
    total_cart_price = "//span[@class='summary-price']"

    add_to_cart = "//div[@class='add-cart']"
    cart = "//a[@href='/site/cart'][contains(text(), 'Оформить')]"
    menu = "//div[@class='bm-burger-button']"
    link_about = "//a[@id='about_sidebar_link']"