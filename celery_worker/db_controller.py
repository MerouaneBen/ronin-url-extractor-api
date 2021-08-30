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
    def upsert_path_url_token(cls, new_token):
        session = db_session()
        # deactivate current active token
        statement = text("""UPDATE urltokens set is_active=:active, updated_date=:updt where is_active = 1""")
        statement = statement.bindparams(active=0,  updt=datetime.datetime.utcnow())
        session.execute(statement)
        session.commit()

        # insert  new active token
        row = {"tk": new_token, "indate": datetime.datetime.utcnow(), "active": 1}
        statement = text("""INSERT INTO urltokens(token, insert_date, is_active) 
                         VALUES(:tk, :indate, :active)""")
        session.execute(statement, **row)
        session.commit()
        # we close session
        session.close()

    @classmethod
    def insert_path_url_token(cls, new_token):
        session = db_session()
        # insert  new active token
        #row = {"tk": new_token, "indate": datetime.datetime.utcnow(), "active": 1}
        statement = text("""INSERT INTO urltokens(token, insert_date, is_active) 
                         VALUES(:tk, :indate, :active)""")
        session.execute(statement, tk=new_token, indate=datetime.datetime.utcnow(), active=1)
        session.commit()
        # we close session
        session.close()