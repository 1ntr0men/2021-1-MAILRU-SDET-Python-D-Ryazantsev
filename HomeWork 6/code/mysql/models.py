from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class First(Base):
    __tablename__ = 'count_of_strings'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<count_of_strings(" \
               f"id='{self.id}'," \
               f"answer='{self.answer}'," \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    answer = Column(Integer, nullable=False)


class Second(Base):
    __tablename__ = 'count_of_get_etc'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<count_of_get_etc(" \
               f"id='{self.id}'," \
               f"req_type='{self.req_type}'," \
               f"amount='{self.amount}'" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    req_type = Column(String(300), nullable=False)
    amount = Column(Integer, nullable=False)


class Third(Base):
    __tablename__ = 'top_ten_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<top_ten_requests(" \
               f"id='{self.id}'," \
               f"url='{self.url}'," \
               f"amount='{self.amount}'" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(50), nullable=False)
    amount = Column(Integer, nullable=False)


class Fourth(Base):
    __tablename__ = 'top_five_400'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<top_five_400(" \
               f"id='{self.id}'," \
               f"url='{self.url}'," \
               f"status='{self.status}'" \
               f"amount='{self.amount}'" \
               f"ip='{self.ip}'" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(300), nullable=False)
    status = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    ip = Column(String(15), nullable=False)


class Fifth(Base):
    __tablename__ = 'top_five_500'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<top_five_500(" \
               f"id='{self.id}'," \
               f"ip='{self.ip}'," \
               f"amount='{self.amount}'" \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(15), nullable=False)
    amount = Column(Integer, nullable=False)
