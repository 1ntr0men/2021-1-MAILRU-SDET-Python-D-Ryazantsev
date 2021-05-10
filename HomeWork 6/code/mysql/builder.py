from mysql.models import First, Second, Third, Fourth, Fifth


class MySQLBuilder:

    def __init__(self, client):
        self.client = client

    def create_in_first(self, answer):
        new_line = First(
            answer=answer,
        )
        self.client.session.add(new_line)
        self.client.session.commit()  # no need if sessionmaker autocommit=True
        return new_line

    def create_in_second(self, req_type, amount):
        new_line = Second(
            req_type=req_type,
            amount=amount
        )
        self.client.session.add(new_line)
        self.client.session.commit()  # no need if sessionmaker autocommit=True
        return new_line

    def create_in_third(self, url, amount):
        new_line = Third(
            url=url,
            amount=amount,
        )
        self.client.session.add(new_line)
        self.client.session.commit()  # no need if sessionmaker autocommit=True
        return new_line

    def create_in_fourth(self, url, status, amount, ip):
        new_line = Fourth(
            url=url,
            status=status,
            amount=amount,
            ip=ip
        )
        self.client.session.add(new_line)
        self.client.session.commit()  # no need if sessionmaker autocommit=True
        return new_line

    def create_in_fifth(self, ip, amount):
        new_line = Fifth(
            ip=ip,
            amount=amount,
        )
        self.client.session.add(new_line)
        self.client.session.commit()  # no need if sessionmaker autocommit=True
        return new_line
