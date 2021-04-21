from base import BaseCase
import basic_locators

import time
import pytest


class TestOne(BaseCase):
    # @pytest.mark.skip("SKIP")
    def test_login(self):
        assert "https://target.my.com/dashboard" in self.driver.current_url

    # @pytest.mark.skip("SKIP")
    def test_logout(self):
        time.sleep(5)  # извините за sleep в следующей работе их не будет)
        self.click(basic_locators.LOGOUT_LOCATOR)
        time.sleep(3)
        self.click(basic_locators.LOGOUT_BUTTON_LOCATOR)
        assert "https://target.my.com/" in self.driver.current_url

    # @pytest.mark.skip("SKIP")
    @pytest.mark.parametrize(
        "buttons, url",
        [
            pytest.param(
                basic_locators.GO_TO_STATISTIC_LOCATOR, "https://target.my.com/statistics/summary"
            ),
            pytest.param(
                basic_locators.GO_TO_BILLING_LOCATOR, "https://target.my.com/billing#deposit"
            )
        ]
    )
    def test_interface_move(self, buttons, url):
        self.click(buttons)
        time.sleep(3)
        assert url in self.driver.current_url

    # @pytest.mark.skip("SKIP")
    def test_edit_info(self):
        self.click(basic_locators.GO_TO_PROFILE_LOCATOR)

        self.write("test test test", basic_locators.FIO_LOCATOR)
        self.write("+11111", basic_locators.TEL_LOCATOR)
        self.write("qwe@qwe.qwe", basic_locators.EMAIL_LOCATOR)

        self.click(basic_locators.SAVE_BUTTON_LOCATOR)

        self.update()

        fio_line = self.get_info(basic_locators.FIO_LOCATOR)
        tel_line = self.get_info(basic_locators.TEL_LOCATOR)
        email_line = self.get_info(basic_locators.EMAIL_LOCATOR)
        assert fio_line == "test test test"
        assert tel_line == "+11111"
        assert email_line == "qwe@qwe.qwe"
