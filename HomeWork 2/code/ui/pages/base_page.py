import allure
from utils.decorators import wait
from ui.locators.basic_locators import BasePageLocators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException

BASE_TIMEOUT = 10
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
        def _click():
            element = self.find(locator, timeout=timeout)
            self.scroll_to(element)
            element.click()
            return True

        return wait(_click, error=ElementNotInteractableException, check=True, timeout=timeout)

    @allure.step("Writing {locator}")
    def write(self, words, locator, timeout=None):
        def _write():
            line = self.find(locator, timeout=timeout)
            self.scroll_to(line)
            line.clear()
            line.send_keys(words)
            return True

        return wait(_write, error=StaleElementReferenceException, check=True, timeout=timeout, interval=0.1)

    @staticmethod
    def format_locator(locator, text):
        return locator[0], locator[1].format(text)
