import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import ChromeOptions

from mysql.sql_client import MysqlClient
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from utils.functions_for_tests import get_valid_name, fake


@pytest.fixture(scope="function")
def driver(test_dir):
    options = ChromeOptions()
    options.add_experimental_option("prefs", {"download.default_directory": test_dir})
    manager = ChromeDriverManager(version='latest')
    url = "http://127.0.0.1:8080"
    browser = webdriver.Chrome(executable_path=manager.install())
    browser.get(url)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture()
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture(scope="function")
def logined_driver(driver):
    username = get_valid_name()
    lp = LoginPage(driver)
    ld = lp.sign_up(get_valid_name(), fake.email(), fake.password())
    yield MainPage(ld)
    sql = MysqlClient(user="test_qa", password="qa_test", db_name="test")
    sql.connect()
    sql.delete_user(username)
