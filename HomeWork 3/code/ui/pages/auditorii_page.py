from selenium.common.exceptions import TimeoutException

from ui.locators.basic_locators import AuditoriiPageLocators
from ui.pages.base_page import BasePage


class AuditoriiPage(BasePage):
    locators = AuditoriiPageLocators()
    url = "https://target.my.com/segments/segments_list"

    def create_segment(self, mode):
        try:
            self.click(self.locators.CREATE_BUTTON_LOCATOR)
        except TimeoutException:
            self.click(self.locators.ALTERNATIVE_CREATE_BUTTON_LOCATOR)

        self.click(self.locators.CHECKBOX_LOCATOR)
        self.click(self.locators.ADD_SEGMENT_BUTTON)
        self.click(self.locators.BUBLE_CLOSE_LOCATOR, timeout=30)
        self.write("test " + mode, self.locators.ADD_SEGMENT_NAME_LOCATOR, timeout=20)
        self.click(self.locators.CREATE_SEGMENT_LOCATOR)

    def check_new_segment(self):
        return self.find(self.locators.CHECK_NEW_SEGMENT_LOCATOR)

    def segment_delete(self, mode):
        locator_find_segment = (self.locators.SEARCH_SEGMENT[0],
                                self.locators.SEARCH_SEGMENT[1].format("test " + mode))
        segment_id = self.find(locator_find_segment, timeout=20).get_attribute("href")[45:]
        locator_checkbox_segment = (self.locators.CHECKBOX_SEGMENT[0],
                                    self.locators.CHECKBOX_SEGMENT[1].format(str(segment_id)))
        self.click(locator_checkbox_segment)
        self.click(self.locators.VUPADASHKA_DELETE_LOCATOR)
        self.click(self.locators.DELETE_BUTTON_V_VUPADASHKE_LOCATOR, timeout=10)

    def check_delete_segment(self):
        return self.find(self.locators.CREATE_BUTTON_LOCATOR)
