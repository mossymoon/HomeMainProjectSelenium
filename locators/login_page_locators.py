# локаторы для авторизации


class LoginPageLocators:
    button_cabinet = "//a[@href='/user/login'][contains(text(), 'Войти')]"
    user_login = "//input[@id='UserLogin_username']"
    user_password = "//input[@id='UserLogin_password']"
    button_enter = "//input[@value='Вход']"
