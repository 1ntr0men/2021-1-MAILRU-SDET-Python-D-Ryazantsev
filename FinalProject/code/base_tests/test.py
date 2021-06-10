import pytest

from base_tests.base import BaseCase
from ui.pages.main_page import MainPage
from utils.functions_for_tests import get_valid_name, get_invalid_name, fake


class TestUI(BaseCase):

    @pytest.mark.UI
    @pytest.mark.parametrize(
        "username, email,  password",
        [
            pytest.param(get_valid_name(), fake.email(), fake.password())
        ]
    )
    def test_sign_in(self, username, email, password):
        lp = self.login_page
        lp.sign_up(username, email, password)
        assert self.mysql.check_availability(username)

        lp.logout()

        lp.sign_in(username, password)
        assert lp.driver.current_url == "http://127.0.0.1:8080/welcome/"

    @pytest.mark.UI
    @pytest.mark.parametrize(
        "username, password, fail_string",
        [
            pytest.param("A" * 17, "password", "Incorrect username length"),
            pytest.param("NoTeXiSt", "password", "Invalid username or password")
        ]
    )
    def test_incorrect_sign_in(self, username, password, fail_string):
        lp = self.login_page
        lp.sign_in(username, password)
        assert lp.check_fail(fail_string)

    @pytest.mark.UI
    @pytest.mark.parametrize(
        "username, email,  password",
        [
            pytest.param(get_valid_name(), fake.email(), fake.password())
        ]
    )
    def test_sign_up(self, username, email, password):
        self.login_page.sign_up(username, email, password)
        assert self.mysql.check_availability(username)
        self.mysql.delete_user(username)

    @pytest.mark.UI
    @pytest.mark.parametrize(
        "username, email,  password, fail_string",
        [
            pytest.param("A" * 17, fake.email(), fake.password(), "Incorrect username length"),
            pytest.param(get_invalid_name(), fake.email(), fake.password(), "Incorrect username length"),
            pytest.param(get_invalid_name(), fake.email(), fake.password(),
                         "Incorrect username length and Passwords must match")
        ]
    )
    def test_incorrect_sign_up(self, username, email, password, fail_string):
        lp = self.login_page
        if fail_string == "Incorrect username length and Passwords must match":
            lp.sign_up(username, email, password, repeat_pass=fake.password())
        else:
            lp.sign_up(username, email, password)
        assert lp.check_fail(fail_string)
        assert not self.mysql.check_availability(username)

    @pytest.mark.UI
    def test_sign_up_existent_user(self):
        username = get_valid_name()
        email = fake.email()
        password = fake.password()
        lp = self.login_page
        lp.sign_up(username, email, password)

        assert self.mysql.check_availability(username)

        lp.logout()

        lp.sign_up(username, email, password)
        assert lp.check_fail("User already exist")

        self.mysql.delete_user(username)

    @pytest.mark.UI
    def test_logged_as(self):
        username = "LOGIN_CHECK"
        lp = self.login_page
        ld = MainPage(lp.sign_up(username, fake.email(), fake.password()))
        assert ld.check_logged_as(username)

    @pytest.mark.UI
    def test_go_python_org(self, logined_driver):
        mp = logined_driver
        mp.go_to_python_org()
        assert mp.driver.current_url == "https://www.python.org/"

    @pytest.mark.UI
    def test_go_to_python_history(self, logined_driver):
        mp = logined_driver
        mp.go_to_head_menu("Python", "Python history")
        assert mp.driver.current_url == "https://en.wikipedia.org/wiki/History_of_Python"

    @pytest.mark.UI
    def test_go_to_about_flask(self, logined_driver):
        mp = logined_driver
        mp.go_to_head_menu("Python", "About Flask")
        assert mp.driver.current_url == "https://flask.palletsprojects.com/en/1.1.x/#"

    @pytest.mark.UI
    def test_go_to_download_centos(self, logined_driver):
        mp = logined_driver
        mp.go_to_head_menu("Linux", "Download Centos7")
        assert mp.driver.current_url == "https://www.centos.org/download/"

    @pytest.mark.UI
    def test_go_to_news(self, logined_driver):
        mp = logined_driver
        mp.go_to_head_menu("Network", "News")
        assert mp.driver.current_url == "https://www.wireshark.org/news/"

    @pytest.mark.UI
    def test_go_to_downloads(self, logined_driver):
        mp = logined_driver
        mp.go_to_head_menu("Network", "Download")
        assert mp.driver.current_url == "https://www.wireshark.org/#download"

    @pytest.mark.UI
    def test_go_to_examples(self, logined_driver):
        mp = logined_driver
        mp.go_to_head_menu("Network", "Examples ")
        assert mp.driver.current_url == "https://hackertarget.com/tcpdump-examples/"

    @pytest.mark.UI
    def test_go_image_api(self, logined_driver):
        mp = logined_driver
        mp.go_image("/static/images/laptop.png")
        assert mp.driver.current_url == "https://en.wikipedia.org/wiki/API"

    @pytest.mark.UI
    def test_go_image_future_of_internet(self, logined_driver):
        mp = logined_driver
        mp.go_image("/static/images/loupe.png")
        assert mp.driver.current_url == "https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/"

    @pytest.mark.UI
    def test_go_image_smtp(self, logined_driver):
        mp = logined_driver
        mp.go_image("/static/images/analytics.png")
        assert mp.driver.current_url == "https://ru.wikipedia.org/wiki/SMTP"

    @pytest.mark.UI
    def test_dzen_python(self, logined_driver):
        dzen = [
            "Beautiful is better than ugly.",
            "Explicit is better than implicit.",
            "Simple is better than complex.",
            "Complex is better than complicated.",
            "Flat is better than nested.",
            "Sparse is better than dense.",
            "Readability counts.",
            "Special cases aren't special enough to break the rules.",
            "Although practicality beats purity.",
            "Errors should never pass silently.",
            "Unless explicitly silenced.",
            "In the face of ambiguity, refuse the temptation to guess.",
            "There should be one-- and preferably only one --obvious way to do it.",
            "Although that way may not be obvious at first unless you're Dutch.",
            "Now is better than never.",
            "Although never is often better than *right* now.",
            "If the implementation is hard to explain, it's a bad idea.",
            "If the implementation is easy to explain, it may be a good idea.",
            "Namespaces are one honking great idea -- let's do more of those!"
        ]
        mp = logined_driver
        count = 0
        for i in range(20):
            if mp.get_dzen() in dzen:
                count += 1
            self.driver.refresh()
        assert count > 0
        print(count)
