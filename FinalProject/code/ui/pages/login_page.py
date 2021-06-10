from ui.locators.basic_locators import LoginPageLocators
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage


class LoginPage(BasePage):
    locator = LoginPageLocators()

    def sign_up(self, username, email, password, repeat_pass=None):
        if not repeat_pass:
            repeat_pass = password

        if self.driver.current_url != "http://127.0.0.1:8080/reg":
            sign_up = self.find(self.locator.CREATE_ACCOUNT_BUTTON_LOCATOR)
            sign_up.click()

        self.write(username, self.locator.USERNAME_LINE_LOCATOR)
        self.write(email, self.locator.EMAIL_LINE_LOCATOR)
        self.write(password, self.locator.PASSWORD_LINE_LOCATOR)
        self.write(repeat_pass, self.locator.REPEAT_PASSWORD_LINE_LOCATOR)

        checkbox = self.find(self.locator.ACCEPT_CHECKBOX_LOCATOR)
        checkbox.click()

        submit = self.find(self.locator.SUBMIT_BUTTON_LOCATOR)
        submit.click()
        return self.driver

    def sign_in(self, username, password):
        self.write(username, self.locator.USERNAME_LINE_LOCATOR)
        self.write(password, self.locator.PASSWORD_LINE_LOCATOR)

        go_button = self.find(self.locator.SUBMIT_BUTTON_LOCATOR)
        go_button.click()
        return self.driver

    def check_fail(self, fail_string):
        fail = self.get_text(self.locator.FAIL_STRING_LOCATOR)
        return fail == fail_string

    def logout(self):
        logout = self.find(self.locator.LOGOUT_BUTTON_LOCATOR)
        logout.click()
