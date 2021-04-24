from stuff.files_path import directory_path
from ui.locators.android_locators import AboutPageANDROIDLocators
from ui.pages.base_page import BasePage


class AboutPage(BasePage):
    locators = AboutPageANDROIDLocators()

    @staticmethod
    def get_version_from_apk():
        import os
        for file in os.listdir(directory_path()):
            if file.endswith(".apk"):
                return file.title()

    def get_version(self):
        return self.get_text(self.locators.VERSION_LOCATOR).split()[1]

    def get_trademark(self):
        return self.get_text(self.locators.COPYRIGHT_LOCATOR)
