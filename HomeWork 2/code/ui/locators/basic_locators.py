from selenium.webdriver.common.by import By


class LoginLocators:
    SIGN_IN_LOCATOR = (By.XPATH, "//div[contains(text(),'Войти')]")
    LOGIN_LOCATOR = (By.NAME, 'email')
    PASSWORD_LOCATOR = (By.NAME, 'password')
    GO_LOCATOR = (By.XPATH, "//div[contains(text(),'Войти') and contains(@class, 'authForm-module')]")


class BasePageLocators:
    GO_TO_AUDITORII_LOCATOR = (By.XPATH, "//a[contains(@class,'center-module-button') and @href= '/segments']")


class DashboardLocators(BasePageLocators):
    CREATE_COMPANY_LOCATOR = (By.XPATH, "//div[contains(text(),'Создать кампанию')]")


class CompanyNewPageLocators(BasePageLocators):
    TRAFFIC_BUTTON_LOCATOR = (By.XPATH, "//div[contains(text(), 'Трафик')]")
    URL_COMPANY_LOCATOR = (By.XPATH, "//input[@placeholder='Введите ссылку']")

    BUDGET_PER_DAY_LOCATOR = (By.XPATH, "//input[@data-test='budget-per_day']")
    BUDGET_TOTAL_LOCATOR = (By.XPATH, "//input[@data-test='budget-total']")

    FORMAT_CARUSEL_LOCATOR = (By.XPATH, "//div[@id='patterns_26']")

    INPUT_600_LOCATOR = (By.XPATH, "//input[@data-test='image_600x600_slide_{}']")
    INPUT_256_LOCATOR = (By.XPATH, "//input[@data-test='icon_256x256']")

    CROPPER_SAVE_PHOTO = (By.XPATH, "//input[contains(@class, 'image-cropper__save')]")

    URL_SLIDE_LOCATOR = (By.XPATH, "//input[@data-name = 'url_slide_{}']")

    TITLE_SLIDE_LOCATOR = (By.XPATH, "//input[@data-name = 'title_25_slide_{}']")

    TITLE_AD_LOCATOR = (By.XPATH, "//input[@data-name = 'title_25']")
    TEXT_AREA_LOCATOR = (By.XPATH, "//textarea[@data-name = 'text_50']")

    COMPLETED_UPLOADED_PHOTO_LOCATOR = (
        By.XPATH,
        "//div[@data-pattern-name = 'carousel_img_full_slide_{}']//div//img[contains(@class, 'carouselSlide')]")

    SAVE_AD_LOCATOR = (By.XPATH, "//div[contains(text(), 'Сохранить объявление')]")

    SELECT_SLIDE_LOCATOR = (By.XPATH, "//li[contains(@class, 'roles-module-') and @data-id={}]")

    CREATE_COMPANY_LOCATOR = (By.XPATH, "//div[contains(text(), 'Создать кампанию')]")

    MY_COMPANY_LOCATOR = (By.XPATH, "//a[contains(@class,'nameCell-module-campaignNameLink') and @title='{}']")

    SET_NAME_COMPANY_LOCATOR = (
        By.XPATH, "//input[@data-translated-attr = 'placeholder' and @class = 'input__inp js-form-element']")

    SHESTERENKA_BUTTON = (
        By.XPATH, "//div[contains(@class, 'main-module-Cell') and contains(@data-test, 'setting-{}')]/div")
    DELETE_BUTTON_IN_SHESTERENKA_LOCATOR = (
        By.XPATH, "//li[contains(@class, 'optionsList-module-option') and @title='Удалить']")


class AuditoriiPageLocators(BasePageLocators):
    CREATE_BUTTON_LOCATOR = (By.XPATH, "//a[@href='/segments/segments_list/new/' and text()='Создайте']")
    ALTERNATIVE_CREATE_BUTTON_LOCATOR = (By.XPATH, "//div[text()='Создать сегмент']")

    CHECKBOX_LOCATOR = (By.XPATH, "//input[@class='adding-segments-source__checkbox js-main-source-checkbox']")
    ADD_SEGMENT_BUTTON = (By.XPATH, "//div[text()='Добавить сегмент']")
    CREATE_SEGMENT_LOCATOR = (By.XPATH, "//div[text()='Создать сегмент' and @class='button__text']")

    ADD_SEGMENT_NAME_LOCATOR = (By.XPATH, "//div[@class='input__wrap']/input[@maxlength='60']")

    CHECK_NEW_SEGMENT_LOCATOR = (
        By.XPATH, "//div[contains(@class, 'page_segments__title') and text()='Список сегментов']")

    SEARCH_SEGMENT = (By.XPATH, "//a[@data-push-state='true' and @title='{}']")

    CHECKBOX_SEGMENT = (By.XPATH,
                        "//div[contains(@class, 'main-module-CellFirst') and contains(@data-test, 'id-{}')]//input[@type='checkbox']")

    VUPADASHKA_DELETE_LOCATOR = (By.XPATH,
                                 "//span[contains(@class, 'select-module-itemInner') and text()='Действия']")
    DELETE_BUTTON_V_VUPADASHKE_LOCATOR = (By.XPATH,
                                          "//li[@title='Удалить' and @data-test='remove']")

    BUBLE_CLOSE_LOCATOR = (By.XPATH, "//span[@class='bubble-ts__x js-bubble-close']")
