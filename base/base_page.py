import datetime

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from locators.base_page_locators import BasePageLocators


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        return get_url

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('/Users/stepa/PycharmProjects/MainProjectSelenium/screen/' + name_screenshot)

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")


