from selenium.webdriver.common.by import By


class BasePageLocators:
    pass


class LoginPageLocators(BasePageLocators):
    USERNAME_LINE_LOCATOR = (By.ID, "username")
    PASSWORD_LINE_LOCATOR = (By.ID, "password")
    EMAIL_LINE_LOCATOR = (By.ID, "email")
    REPEAT_PASSWORD_LINE_LOCATOR = (By.ID, "confirm")

    SUBMIT_BUTTON_LOCATOR = (By.ID, "submit")
    CREATE_ACCOUNT_BUTTON_LOCATOR = (By.XPATH, "//a[contains(text(),'Create an account')]")
    LOGOUT_BUTTON_LOCATOR = (By.XPATH, "//a[contains(text(),'Logout')]")

    ACCEPT_CHECKBOX_LOCATOR = (By.ID, "term")

    FAIL_STRING_LOCATOR = (By.ID, "flash")


class MainPageLocators(BasePageLocators):
    TOP_MENU_LOCATOR = (By.XPATH, "//a[text()='{}']")
    IMAGE_LOCATOR = (By.XPATH, "//img[contains(@src, '{}')]")

    LOGGED_AS_LOCATOR = (By.XPATH, "//li[contains(text(),'Logged as')]")

    DZEN_OF_PYTHON_LOCATOR = (By.XPATH, "//div/p[text()!='powered by ТЕХНОАТОМ']")
