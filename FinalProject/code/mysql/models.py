from sqlalchemy import Column, Integer,  Date, ForeignKey, VARCHAR, String, SmallInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TestUsers(Base):
    __tablename__ = 'test_users'
    __table_args__ = {'mysql_charset': 'utf8'}

    def repr(self):
        return f"<TestUsers(" \
               f"id='{self.id}'," \
               f"username='{self.username}', " \
               f"password='{self.password}', " \
               f"email={self.email}" \
               f"access='{self.access}'" \
               f"active='{self.active}'" \
               f"start_active_item='{self.start_active_item}'" \
               f")>"

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    username = Column(VARCHAR(16), default=None, unique=True)
    password = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(64), nullable=False, unique=True)
    access = Column(SmallInteger, default=None)
    active = Column(SmallInteger, default=None)
    start_active_time = Column(Date, default=None, primary_key="id")
