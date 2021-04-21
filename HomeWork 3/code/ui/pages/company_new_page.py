import time

from ui.locators.basic_locators import CompanyNewPageLocators
from ui.pages.base_page import BasePage
from files.files_path import files_path
from selenium.webdriver.support import expected_conditions as EC


class CompanyNewPage(BasePage):
    locator = CompanyNewPageLocators()
    url = "https://target.my.com/campaign/new"

    def create_company(self):
        self.select_company()
        self.select_budget()
        self.select_format()
        self.select_slaids()
        self.write("test test test", self.locator.SET_NAME_COMPANY_LOCATOR)
        time.sleep(3)
        self.click(self.locator.CREATE_COMPANY_LOCATOR)

    def select_company(self):
        self.click(self.locator.TRAFFIC_BUTTON_LOCATOR, timeout=30)
        self.write("https://vk.com/youtubeupload", self.locator.URL_COMPANY_LOCATOR)

    def select_budget(self):
        self.write("100", self.locator.BUDGET_PER_DAY_LOCATOR)
        self.write("200", self.locator.BUDGET_TOTAL_LOCATOR)

    def select_format(self):
        self.click(self.locator.FORMAT_CARUSEL_LOCATOR)

    def select_slaids(self):
        file256 = files_path("256_256.jpg")
        self.upload_photo(self.locator.INPUT_256_LOCATOR, file256, check=False)
        self.write("Ad_title", self.locator.TITLE_AD_LOCATOR)
        self.write("Ad_description", self.locator.TEXT_AREA_LOCATOR)

        for i in range(3):
            self.fill_slide(i)

    def fill_slide(self, i):
        file600 = files_path("600_600.png")
        locator_select_slide = (self.locator.SELECT_SLIDE_LOCATOR[0],
                                self.locator.SELECT_SLIDE_LOCATOR[1].format(str(i)))
        locator_600_slide = (self.locator.INPUT_600_LOCATOR[0],
                             self.locator.INPUT_600_LOCATOR[1].format(str(i + 1)))
        locator_url_slide = (self.locator.URL_SLIDE_LOCATOR[0],
                             self.locator.URL_SLIDE_LOCATOR[1].format(str(i + 1)))
        locator_title_slide = (self.locator.TITLE_SLIDE_LOCATOR[0],
                               self.locator.TITLE_SLIDE_LOCATOR[1].format(str(i + 1)))
        self.click(locator_select_slide)
        self.upload_photo(locator_600_slide, file600, i=i)
        self.write("https://vk.com/youtubearchiv", locator_url_slide)
        self.write("Название " + str(i + 1), locator_title_slide)

    def upload_photo(self, locator, file_path, check=True, i=0):
        upload_element = self.find(locator)
        self.scroll_to(upload_element)
        upload_element.send_keys(file_path)
        if check:
            locator_complet_load = (self.locator.COMPLETED_UPLOADED_PHOTO_LOCATOR[0],
                                    self.locator.COMPLETED_UPLOADED_PHOTO_LOCATOR[1].format(str(i + 1)))
            self.wait(30).until(EC.presence_of_element_located(locator_complet_load))

    def check_new_company(self):
        return self.find(self.locator.MY_COMPANY_LOCATOR)

    def company_delete(self):
        self.click(self.locator.SHESTERENKA_BUTTON)
        self.click(self.locator.DELETE_BUTTON_IN_SHESTERENKA_LOCATOR)
        self.driver.refresh()
