import allure
import logging
from utils.decorators import wait
from ui.locators.basic_locators import BasePageLocators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

BASE_TIMEOUT = 3
CLICK_RETRY = 5


class PageNotLoadedException(Exception):
    pass


class BasePage(object):
    url = "https://target.my.com/"
    locator = BasePageLocators()

    def __init__(self, driver):
        self.driver = driver
        assert self.is_opened()

    def is_opened(self):
        def _check_url():
            if self.driver.current_url != self.url:
                raise PageNotLoadedException(
                    f'{self.url} did not opened in {BASE_TIMEOUT} for {self.__class__.__name__}.\n'
                    f'Current url: {self.driver.current_url}.')
            return True

        return wait(_check_url, error=PageNotLoadedException, check=True, timeout=BASE_TIMEOUT, interval=0.1)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true)", element)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    @allure.step("Clicking {locator}")
    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator, timeout=timeout)
                self.scroll_to(element)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def write(self, words, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                line = self.find(locator, timeout=timeout)
                self.scroll_to(line)
                line = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                line.clear()
                line.send_keys(words)
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

