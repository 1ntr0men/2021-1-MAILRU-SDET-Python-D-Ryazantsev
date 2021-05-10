from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class First(Base):
    __tablename__ = 'First number'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<First number(" \
               f"answer='{self.answer}'," \
               f")>"

    answer = Column(Integer, nullable=False)


class Second(Base):
    __tablename__ = 'Second number'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Second number(" \
               f"type='{self.req_type}'," \
               f"amount='{self.amount}'" \
               f")>"

    req_type = Column(String(300), nullable=False)
    amount = Column(Integer, nullable=False)


class Third(Base):
    __tablename__ = 'Third number'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Third number(" \
               f"url='{self.url}'," \
               f"amount='{self.amount}'" \
               f")>"

    url = Column(String(50), nullable=False)
    amount = Column(Integer, nullable=False)


class Fourth(Base):
    __tablename__ = 'Fourth number'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Fourth number(" \
               f"url='{self.url}'," \
               f"status='{self.status}'" \
               f"amount='{self.amount}'" \
               f"ip='{self.ip}'" \
               f")>"

    url = Column(String(300), nullable=False)
    status = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    ip = Column(String(15), nullable=False)


class Fifth(Base):
    __tablename__ = 'Fifth number'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Fifth number(" \
               f"ip='{self.ip}'," \
               f"amount='{self.amount}'" \
               f")>"

    ip = Column(String(15), nullable=False)
    amount = Column(Integer, nullable=False)
