import os

import allure
import pytest

from appium import webdriver

from ui.capability import capability_select
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage


class UnsupportedBrowserType(Exception):
    pass


@pytest.fixture
def base_page(driver, config):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver, config):
    return MainPage(driver=driver)


def get_driver(appium_url):
    desired_caps = capability_select()
    driver = webdriver.Remote(appium_url, desired_capabilities=desired_caps)
    return driver


@pytest.fixture(scope='function')
def driver(config, test_dir):
    appium_url = config['appium']
    browser = get_driver(appium_url)
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def ui_report(driver, request, test_dir, config):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        screenshot_file = os.path.join(test_dir, 'failure.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'failure.png', attachment_type=allure.attachment_type.PNG)
