import os

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.dashboard_page import DashboardPage
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from selenium.webdriver import ChromeOptions


@pytest.fixture()
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture()
def dashboard_page(driver):
    return DashboardPage(driver=driver)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture(scope="function")
def driver(test_dir):
    options = ChromeOptions()
    options.add_experimental_option("prefs", {"download.default_directory": test_dir})
    manager = ChromeDriverManager(version='latest')
    url = "https://target.my.com/"
    browser = webdriver.Chrome(executable_path=manager.install())
    browser.get(url)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def logined_driver(driver):
    logined_driver = LoginPage(driver)
    dashboard_page = logined_driver.sign_in("intromenoff@gmail.com", "intromen")
    return dashboard_page


@pytest.fixture(scope="session")
def repo_root():
    os.path.abspath(os.path.join(__file__, os.pardir))


@pytest.fixture(scope='function', autouse=True)
def ui_report(driver, request, test_dir):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        screenshot_file = os.path.join(test_dir, 'failure.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'failure.png', attachment_type=allure.attachment_type.PNG)

        browser_logfile = os.path.join(test_dir, 'browser.log')
        with open(browser_logfile, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n\n")

        with open(browser_logfile, 'r') as f:
            allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)
