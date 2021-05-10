import pytest

from mysql.builder import MySQLBuilder
from fifth_HW import fifth_HW
from mysql.models import First, Second, Third, Fourth, Fifth


class MySQLBase:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql = mysql_client
        self.mysql_builder = MySQLBuilder(mysql_client)

        self.prepare()


class TestFirst(MySQLBase):

    def prepare(self):
        self.mysql_builder.create_in_first(fifth_HW.first_number())

    def test(self):
        answer = self.mysql.session.query(First).first().answer
        assert answer == 225133


class TestSecond(MySQLBase):

    def prepare(self):
        for req_type, amount in fifth_HW.second_number().items():
            self.mysql_builder.create_in_second(req_type=req_type, amount=amount)

    def test(self):
        assert len(self.mysql.session.query(Second).all()) == 5


class TestThird(MySQLBase):

    def prepare(self):
        for item in fifth_HW.third_number():
            self.mysql_builder.create_in_third(url=item[0], amount=item[1])

    def test(self):
        assert len(self.mysql.session.query(Third).all()) == 10


class TestFourth(MySQLBase):

    def prepare(self):
        for item in fifth_HW.fourth_number():
            self.mysql_builder.create_in_fourth(url=item[0], status=item[1], amount=item[2], ip=item[3])

    def test(self):
        assert len(self.mysql.session.query(Fourth).all()) == 5


class TestFifth(MySQLBase):

    def prepare(self):
        for item in fifth_HW.fifth_number():
            self.mysql_builder.create_in_fifth(ip=item[0], amount=item[1])

    def test(self):
        assert len(self.mysql.session.query(Fourth).all()) == 5
