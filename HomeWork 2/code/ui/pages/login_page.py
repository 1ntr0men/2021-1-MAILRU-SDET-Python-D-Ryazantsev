from ui.pages.base_page import BasePage
from ui.locators.basic_locators import LoginLocators
from ui.pages.dashboard_page import DashboardPage


class LoginPage(BasePage):
    locator = LoginLocators()
    url = "https://target.my.com/"

    def sign_in(self, login, password):
        sign_in_button = self.find(self.locator.SIGN_IN_LOCATOR)
        sign_in_button.click()

        self.write(login, self.locator.LOGIN_LOCATOR)
        self.write(password, self.locator.PASSWORD_LOCATOR)

        go_button = self.find(self.locator.GO_LOCATOR)
        go_button.click()
        if login == "intromenoff@gmail.com" and password == "intromen":  # если данные валидны
            return DashboardPage(self.driver)


def get_driver(self):
    return self.driver
