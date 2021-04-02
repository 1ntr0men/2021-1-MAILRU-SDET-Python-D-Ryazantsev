from selenium.webdriver.common.by import By

SIGN_IN_LOCATOR = (By.XPATH, "//div[contains(text(),'Войти')]")
LOGIN_LOCATOR = (By.NAME, 'email')
PASSWORD_LOCATOR = (By.NAME, 'password')
GO_LOCATOR = (By.XPATH, "//div[contains(text(),'Войти') and contains(@class, 'authForm-module')]")

GO_TO_PROFILE_LOCATOR = (By.XPATH, "//a[contains(@class,'center-module-profile')]")
GO_TO_BILLING_LOCATOR = (By.XPATH, "//a[contains(@class, 'center-module-billing')]")
GO_TO_STATISTIC_LOCATOR = (By.XPATH, "//a[contains(@class, 'center-module-statistics')]")

FIO_LOCATOR = (By.XPATH, "//div[contains(@class,'js-contacts-field-name')]//input")
TEL_LOCATOR = (By.XPATH, "//div[contains(@class,'js-contacts-field-phone')]//input")
EMAIL_LOCATOR = (By.XPATH, "//div[contains(@class,'js-additional-email')]//input")

SAVE_BUTTON_LOCATOR = (By.CLASS_NAME, 'button__text')

LOGOUT_LOCATOR = (By.XPATH, "//div[starts-with(@class,'right-module-rightButton')]")
LOGOUT_BUTTON_LOCATOR = (
    By.XPATH, "//a[contains(@class, 'rightMenu-module-rightMenuLink') and text()='Выйти']")
