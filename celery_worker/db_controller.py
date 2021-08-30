import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.sql import text
from config import *

engine = create_engine("mariadb+mariadbconnector://" + MYSQL_USER + ":" + MYSQL_PASSWORD + "@" + MYSQL_HOST + ":" +
                       MYSQL_PORT + "/" + MYSQL_DATABASE, convert_unicode=True)

db_session = scoped_session(sessionmaker(bind=engine))


class RoninUrlPathController:

    @classmethod
    def get_active_path_url_token(cls):
        session = db_session()
        select = text("""select token from urltokens where is_active = 1""")
        active_token = session.execute(select).fetchone()
        session.close()
        if active_token:
            return active_token
        else:
            return None

    @classmethod
    def insert_path_url_token(cls, new_token):
        session = db_session()
        # deactivate current active token
        statement = text("""UPDATE urltokens set is_active=:is_active, updated_date=:updt where is_active = 1""")
        statement = statement.bindparams(is_active=0,  updt=datetime.datetime.utcnow())
        session.execute(statement)
        session.commit()

        # insert  new active token
        row = {"insert_date": datetime.datetime.utcnow(), "is_active": 1, "token": new_token}
        statement = text("""INSERT INTO urltokens(insert_date, is_active, token) 
                         VALUES(:insert_date, :is_active, :token)""")
        session.execute(statement, **row)
        session.commit()
        # we close session
        session.close()
