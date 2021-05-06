from base_tests.base import BaseCase
import pytest


class TestOne(BaseCase):
    @pytest.mark.UI
    @pytest.mark.parametrize(
        "login, password, url",
        [
            pytest.param("asdfasd", "dfsafasd",
                         "https://target.my.com/"),

            pytest.param("intromenoff@gmail.com", "asdlfjsdfklajsd",
                         "https://account.my.com/login/?error_code=1")
        ]
    )
    def test_negative_sign_in(self, login, password, url):
        self.login_page.sign_in(login, password)
        assert url in self.driver.current_url

    @pytest.mark.UI
    def test_logined_fixture(self, logined_driver):
        dashboard_page = logined_driver
        assert dashboard_page.get_url() == "https://target.my.com/dashboard"

    @pytest.mark.UI
    def test_create_company(self, logined_driver):
        dashboard_page = logined_driver
        add_company_page = dashboard_page.go_to_add_company()
        company_name = add_company_page.create_company()
        add_company_page.check_new_company(company_name=company_name)
        add_company_page.company_delete(company_name=company_name)

    @pytest.mark.UI
    def test_create_segment(self, logined_driver):
        dashboard_page = logined_driver
        auditorii_page = dashboard_page.go_to_auditorii()
        segment_name = auditorii_page.create_segment(mode="create")
        assert auditorii_page.check_segment(segment_name)

        auditorii_page.segment_delete(segment_name)

    @pytest.mark.UI
    def test_delete_segment(self, logined_driver):
        dashboard_page = logined_driver
        auditorii_page = dashboard_page.go_to_auditorii()
        segment_name = auditorii_page.create_segment(mode="delete")

        auditorii_page.segment_delete(segment_name)
        assert not auditorii_page.check_segment(segment_name)
