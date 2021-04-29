import time

from selenium.common.exceptions import TimeoutException

from ui.locators.basic_locators import AuditoriiPageLocators
from ui.pages.base_page import BasePage


class AuditoriiPage(BasePage):
    locators = AuditoriiPageLocators()
    url = "https://target.my.com/segments/segments_list"

    def create_segment(self, mode):
        try:
            self.click(self.locators.CREATE_BUTTON_LOCATOR)
        except TimeoutError:
            self.click(self.locators.ALTERNATIVE_CREATE_BUTTON_LOCATOR)
        segment_name = time.strftime("%H:%M:%S", time.localtime()) + " Segment " + mode

        self.click(self.locators.CHECKBOX_LOCATOR)
        self.click(self.locators.ADD_SEGMENT_BUTTON)
        self.write(segment_name, self.locators.ADD_SEGMENT_NAME_LOCATOR, timeout=20)
        self.click(self.locators.CREATE_SEGMENT_LOCATOR)
        return segment_name

    def check_segment(self, segment_name):
        locator_find_segment = self.format_locator(self.locators.SEARCH_SEGMENT, segment_name)
        try:
            self.find(locator_find_segment, timeout=20)
            return True
        except TimeoutException:
            return False

    def segment_delete(self, segment_name):
        locator_find_segment = self.format_locator(self.locators.SEARCH_SEGMENT, segment_name)
        segment_id = self.find(locator_find_segment, timeout=20).get_attribute("href")[45:]
        locator_checkbox_segment = self.format_locator(self.locators.CHECKBOX_SEGMENT, str(segment_id))
        self.click(locator_checkbox_segment)
        self.click(self.locators.VUPADASHKA_DELETE_LOCATOR)
        self.click(self.locators.DELETE_BUTTON_V_VUPADASHKE_LOCATOR, timeout=10)

