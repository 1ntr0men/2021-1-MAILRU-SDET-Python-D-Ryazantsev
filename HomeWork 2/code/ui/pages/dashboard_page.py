from ui.pages.auditorii_page import AuditoriiPage
from ui.pages.base_page import BasePage
from ui.locators.basic_locators import DashboardLocators
from ui.pages.company_new_page import CompanyNewPage


class DashboardPage(BasePage):
    locator = DashboardLocators()
    url = "https://target.my.com/dashboard"

    def go_to_add_company(self):
        self.click(self.locator.CREATE_COMPANY_LOCATOR)
        return CompanyNewPage(self.driver)

    def get_url(self):
        return self.driver.current_url

    def go_to_auditorii(self):
        self.click(self.locator.GO_TO_AUDITORII_LOCATOR)
        return AuditoriiPage(self.driver)
