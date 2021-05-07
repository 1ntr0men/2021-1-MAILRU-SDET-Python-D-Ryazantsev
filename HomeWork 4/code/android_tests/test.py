import pytest
from android_tests.base_test import BaseCase


class TestMarussia(BaseCase):
    @pytest.mark.AndroidUI
    def test_keyboard_input(self):
        main_page = self.main_page
        main_page.main_input("Russia")
        assert main_page.get_title("down") == "Россия"
        main_page.click_on_carousel("население россии")
        assert main_page.get_title("up") == "146 млн."

    @pytest.mark.AndroidUI
    def test_calculator(self):
        main_page = self.main_page
        main_page.main_input("12+43")
        assert main_page.get_answer() == "55"

    @pytest.mark.AndroidUI
    def test_news_source(self):
        settings_page = self.main_page.go_to_settings()
        settings_page.select_news_source()
        assert settings_page.check_news_source() == "Вести ФМ"

    @pytest.mark.AndroidUI
    def test_version(self):
        about_page = self.main_page.go_to_settings().go_to_version_page()
        assert about_page.get_version() in about_page.get_version_from_apk()
        assert "Все права защищены" in about_page.get_trademark()
