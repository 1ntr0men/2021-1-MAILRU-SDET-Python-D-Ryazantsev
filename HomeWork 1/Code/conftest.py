import pytest
from selenium import webdriver
import basic_locators


@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Chrome(executable_path="C:\\Users\\intromen\\Documents\\Projects\\Mail\\chromedriver")
    browser.get("https://target.my.com/")
    browser.maximize_window()
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def logined_driver(driver):
    browser = driver

    sign_in_button = browser.find_element(*basic_locators.SIGN_IN_LOCATOR)
    sign_in_button.click()

    login_line = browser.find_element(*basic_locators.LOGIN_LOCATOR)
    password_line = browser.find_element(*basic_locators.PASSWORD_LOCATOR)

    login_line.clear()
    password_line.clear()

    login_line.send_keys("intromenoff@gmail.com")
    password_line.send_keys("intromen")

    go_button = browser.find_element(*basic_locators.GO_LOCATOR)
    go_button.click()
    yield browser
