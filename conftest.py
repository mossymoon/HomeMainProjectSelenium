import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import Login_page

url = 'https://domkniginn.ru/'

def __init__(self, driver):
    super().__init__(driver)
    self.driver = driver

@pytest.fixture()
def driver():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='/Users/stepa/PycharmProjects/resourse/chromedriver', chrome_options=options)
    yield driver
    # driver = webdriver.Firefox(executable_path='/Users/stepa/PycharmProjects/SeleniumPython23/geckodriver')

@pytest.fixture()
def auth(driver):
    print("Start Test 1")
    login = Login_page(driver)
    yield login.authorization()
