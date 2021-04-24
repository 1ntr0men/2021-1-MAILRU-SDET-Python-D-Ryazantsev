from ui.locators.android_locators import MainPageANDROIDLocator
from ui.pages.base_page import BasePage
from ui.pages.settings_page import SettingsPage


class MainPage(BasePage):
    locators = MainPageANDROIDLocator()

    def get_title(self, direction):
        self.swipe_to_element(self.locators.CARD_TITLE_LOCATOR, 2, direction)
        return self.get_text(self.locators.CARD_TITLE_LOCATOR)

    def click_on_carousel(self, text):
        locator_of_element_in_carousel = (self.locators.ELEMENT_IN_CARUSEL_LOCATOR[0],
                                          self.locators.ELEMENT_IN_CARUSEL_LOCATOR[1].format(text))
        self.swipe_to_element_in_carousel(locator_of_element_in_carousel, 5)
        self.click(locator_of_element_in_carousel)

    def get_answer(self):
        return self.get_text(self.locators.ANSWER_INTEGER_LOCATOR)

    def go_to_settings(self):
        self.click(self.locators.GO_TO_SETTINGS_LOCATOR)
        return SettingsPage(self.driver)
