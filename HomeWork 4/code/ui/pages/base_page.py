import logging
import allure

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.locators.android_locators import BasePageANDROIDLocator

CLICK_RETRY = 3
BASE_TIMEOUT = 5
logger = logging.getLogger('test')


class BasePage(object):
    locators = BasePageANDROIDLocator()

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Clicking {locator}')
    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            logger.info(f'Clicking on {locator}. Try {i + 1} of {CLICK_RETRY}...')
            try:
                element = self.find(locator, timeout=timeout)
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
                line = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                line.clear()
                line.send_keys(words)
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def get_text(self, locator):
        element = self.find(locator)
        return element.get_attribute("text")

    def get_bounds(self, locator):
        element = self.find(locator)
        return element.location

    def swipe(self, direction, swipetime=200):
        """
        Базовый метод свайпа по вертикали
        Описание работы:
        1. узнаем размер окна телефона
        2. Задаем за X - центр нашего экрана
        3. Указываем координаты откуда и куда делать свайп
        4. TouchAction нажимает на указанные стартовые координаты, немного ждет и передвигает нас из одной точки в другую.
        5. release() наши пальцы с экрана, а perform() выполняет всю эту цепочку команд.
        """
        action = TouchAction(self.driver)
        dimension = self.driver.get_window_size()
        x = int(dimension['width'] / 2)
        if direction == "up":
            start_y = int(dimension['height'] * 0.4)
            end_y = int(dimension['height'] * 0.2)
        elif direction == "down":
            start_y = int(dimension['height'] * 0.2)
            end_y = int(dimension['height'] * 0.4)
        action. \
            press(x=x, y=start_y). \
            wait(ms=swipetime). \
            move_to(x=x, y=end_y). \
            release(). \
            perform()

    def swipe_to_element(self, locator, max_swipes, direction):
        """
        :param locator: локатор, который мы ищем
        :param max_swipes: количество свайпов до момента, пока тест не перестанет свайпать вверх
        """
        already_swiped = 0
        while len(self.driver.find_elements(*locator)) == 0:
            if already_swiped > max_swipes:
                raise TimeoutException(f"Error with {locator}, please check function")
            self.swipe(direction=direction)
            already_swiped += 1

    def swipe_left(self, y, swipetime=200):
        """
        Базовый метод свайпа по вертикали
        Описание работы:
        1. узнаем размер окна телефона
        2. Задаем за X - центр нашего экрана
        3. Указываем координаты откуда и куда делать свайп
        4. TouchAction нажимает на указанные стартовые координаты, немного ждет и передвигает нас из одной точки в другую.
        5. release() наши пальцы с экрана, а perform() выполняет всю эту цепочку команд.
        """
        action = TouchAction(self.driver)
        dimension = self.driver.get_window_size()
        start_x = int(dimension['width'] * 0.8)
        end_x = int(dimension['width'] * 0.2)
        action. \
            press(x=start_x, y=y). \
            wait(ms=swipetime). \
            move_to(x=end_x, y=y). \
            release(). \
            perform()

    def swipe_to_element_in_carousel(self, locator, max_swipes):
        """
        :param locator: локатор, который мы ищем
        :param max_swipes: количество свайпов до момента, пока тест не перестанет свайпать вверх
        """
        self.swipe_to_element(self.locators.SUGGEST_LIST_LOCATOR, 2, "up")
        y = self.get_bounds(self.locators.SUGGEST_LIST_LOCATOR)["y"] + 10
        already_swiped = 0
        while len(self.driver.find_elements(*locator)) == 0:
            if already_swiped > max_swipes:
                raise TimeoutException(f"Error with {locator}, please check function")
            self.swipe_left(y)
            already_swiped += 1

    def open_keyboard(self):
        self.click(self.locators.KEYBOARD_BUTTON_LOCATOR)

    def main_input(self, search):
        self.click(self.locators.KEYBOARD_BUTTON_LOCATOR)
        self.write(search, self.locators.MAIN_INPUT_LOCATOR)
        self.click(self.locators.ENTER_BUTTON_LOCATOR)
