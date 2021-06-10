import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

from mysql.models import TestUsers

from mysql.models import Base


class MysqlClient:

    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = '127.0.0.1'
        self.port = 3306

        self.engine = None
        self.connection = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''

        self.engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}',
            encoding='utf8'
        )
        self.connection = self.engine.connect()
        self.session = sessionmaker(bind=self.connection.engine,
                                    autocommit=False,  # use autocommit on session.add
                                    expire_on_commit=False  # expire model after commit (requests data from database)
                                    )()

    def execute_query(self, query, fetch=True):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def delete_user(self, username):
        self.session.query(TestUsers).filter_by(username=username).delete()
        self.session.commit()

    def check_availability(self, username):
        self.session.commit()
        return self.session.query(TestUsers).filter_by(username=username).first()

    def recreate_db(self):
        self.connect(db_created=False)
        self.execute_query(f'DROP database if exists {self.db_name}', fetch=False)
        self.execute_query(f'CREATE database {self.db_name}', fetch=False)
        self.connection.close()

    def create_test_users(self):
        if not inspect(self.engine).has_table('test_users'):
            Base.metadata.tables['test_users'].create(self.engine)

    def clear_test_users(self):
        self.session.query(TestUsers).delete()
        self.session.commit()
