from selenium.webdriver.common.by import By


class BasePageANDROIDLocator:
    SUGGEST_LIST_LOCATOR = (By.ID, "ru.mail.search.electroscope:id/suggests_list")
    KEYBOARD_BUTTON_LOCATOR = (By.ID, "ru.mail.search.electroscope:id/keyboard")
    MAIN_INPUT_LOCATOR = (By.ID, "ru.mail.search.electroscope:id/input_text")
    ENTER_BUTTON_LOCATOR = (By.ID, "ru.mail.search.electroscope:id/text_input_action")


class MainPageANDROIDLocator(BasePageANDROIDLocator):
    CARD_TITLE_LOCATOR = (By.ID, "ru.mail.search.electroscope:id/item_dialog_fact_card_title")

    ELEMENT_IN_CARUSEL_LOCATOR = (By.XPATH, "//android.widget.TextView[contains(@text, '{}')]")

    ANSWER_INTEGER_LOCATOR = (By.XPATH,
                              "//androidx.recyclerview.widget.RecyclerView/android.widget.TextView[@resource-id='ru.mail.search.electroscope:id/dialog_item']")

    GO_TO_SETTINGS_LOCATOR = (By.ID, "ru.mail.search.electroscope:id/assistant_menu_bottom")


class SettingsPageANDROIDLocators(BasePageANDROIDLocator):
    NEWS_SOURCE_LOCATOR = (By.ID, "ru.mail.search.electroscope:id/user_settings_field_news_sources")

    VESTI_FM_LOCATOR = (By.XPATH, "//android.widget.TextView[@text='Вести FM']")

    GALOCHKA_LOCATOR = (By.ID, "ru.mail.search.electroscope:id/news_sources_item_selected")

    BACK_BUTTON_LOCATOR = (By.XPATH, "//android.widget.ImageButton")

    CLOSE_SETTINGS_BUTTON = (By.XPATH, "//android.widget.LinearLayout/android.widget.ImageButton")
    PLAYER_TRACK_NAME_LOCATOR = (By.ID, "ru.mail.search.electroscope:id/player_track_name")
    ABOUT_BUTTON_LOCATOR = (By.ID, "ru.mail.search.electroscope:id/user_settings_about")


class AboutPageANDROIDLocators(BasePageANDROIDLocator):
    VERSION_LOCATOR = (By.ID, "ru.mail.search.electroscope:id/about_version")
    COPYRIGHT_LOCATOR = (By.ID, "ru.mail.search.electroscope:id/about_copyright")
