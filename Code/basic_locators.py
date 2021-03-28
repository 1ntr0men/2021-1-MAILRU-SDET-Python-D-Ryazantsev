from selenium.webdriver.common.by import By

SIGN_IN_LOCATOR = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
LOGIN_LOCATOR = (By.NAME, 'email')
PASSWORD_LOCATOR = (By.NAME, 'password')
GO_LOCATOR = (By.CLASS_NAME, 'authForm-module-button-2G6lZu')

GO_TO_PROFILE_LOCATOR = (By.XPATH, "//a[contains(@class,'center-module-profile-BHql9z')]")
GO_TO_BILLING_LOCATOR = (By.XPATH, "//a[contains(@class, 'center-module-billing-x3wyL6')]")
GO_TO_STATISTIC_LOCATOR = (By.XPATH, "//a[contains(@class, 'center-module-statistics-26_XmT')]")

FIO_LOCATOR = (By.XPATH, "//div[contains(@class,'js-contacts-field-name')]//input[starts-with(@class,'input__inp')]")
TEL_LOCATOR = (By.XPATH, "//div[contains(@class,'js-contacts-field-phone')]//input[starts-with(@class,'input__inp')]")
EMAIL_LOCATOR = (By.XPATH, "//div[contains(@class,'js-additional-email')]//input[starts-with(@class,'input__inp')]")

SAVE_BUTTON_LOCATOR = (By.CLASS_NAME, 'button__text')

LOGOUT_LOCATOR = (By.XPATH, "//div[starts-with(@class,'right-module-rightButton-39YRvc right-module-mail-25NVA9')]")
LOGOUT_BUTTON_LOCATOR = (
    By.XPATH, "//a[@class='rightMenu-module-rightMenuLink-2FYb2O' and text()='Выйти']")
