from ui.locators.android_locators import SettingsPageANDROIDLocators
from ui.pages.about_page import AboutPage
from ui.pages.base_page import BasePage


class SettingsPage(BasePage):
    locators = SettingsPageANDROIDLocators()

    def select_news_source(self):
        self.swipe_to_element(self.locators.NEWS_SOURCE_LOCATOR, 3, direction="up")
        self.click(self.locators.NEWS_SOURCE_LOCATOR)
        self.click(self.locators.VESTI_FM_LOCATOR)
        assert self.find(self.locators.GALOCHKA_LOCATOR)
        self.click(self.locators.BACK_BUTTON_LOCATOR)

    def check_news_source(self):
        self.click(self.locators.CLOSE_SETTINGS_BUTTON)
        self.main_input("News")
        return self.get_text(self.locators.PLAYER_TRACK_NAME_LOCATOR)

    def go_to_version_page(self):
        self.swipe_to_element(self.locators.ABOUT_BUTTON_LOCATOR, 5, "up")
        self.click(self.locators.ABOUT_BUTTON_LOCATOR)
        return AboutPage(self.driver)
