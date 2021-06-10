import time

from ui.locators.basic_locators import MainPageLocators
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    url = "http://127.0.0.1:8080/welcome/"
    locator = MainPageLocators()

    def go_to_python_org(self):
        locator_python_org = self.format_locator(self.locator.TOP_MENU_LOCATOR, "Python")
        link = self.find(locator_python_org)
        link.click()

    def go_to_head_menu(self, frst, scnd):
        locator_frst = self.format_locator(self.locator.TOP_MENU_LOCATOR, frst)
        locator_scnd = self.format_locator(self.locator.TOP_MENU_LOCATOR, scnd)

        self.move_to_element(locator_frst)
        link = self.find(locator_scnd)
        link.click()

        if len(self.driver.window_handles) > 1:
            self.driver.switch_to_window(self.driver.window_handles[1])

    def go_image(self, path):
        locator_image_api = self.format_locator(self.locator.IMAGE_LOCATOR, path)

        link = self.find(locator_image_api)
        link.click()

        self.driver.switch_to_window(self.driver.window_handles[1])

    def check_logged_as(self, username):
        return username in self.get_text(self.locator.LOGGED_AS_LOCATOR)

    def get_dzen(self):
        return self.get_text(self.locator.DZEN_OF_PYTHON_LOCATOR)
