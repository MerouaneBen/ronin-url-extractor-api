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
        updt = datetime.datetime.utcnow()
        statement = text("""UPDATE urltokens set is_active=:active, updated_date=:updt where is_active = 1""")
        statement = statement.bindparams(active=0,  updt=updt)
        session.execute(statement, {"active": 1, "updt": updt})
        session.commit()

        # insert  new active token
        indate = datetime.datetime.utcnow()
        statement = text("""INSERT INTO urltokens(token, insert_date, is_active) VALUES(:tk, :indate, :active)""")
        bind_param_st = statement.bindparams(tk=new_token, indate=indate, active=1)
        session.execute(bind_param_st, {"tk": new_token, "indate": indate, "active": 1})
        session.commit()

        # we close session
        session.close()

    @classmethod
    def insert_path_url_token(cls, new_token):
        session = db_session()
        # insert  new active token
        indate = datetime.datetime.utcnow()
        statement = text("""INSERT INTO urltokens(token, insert_date, is_active) VALUES(:tk, :indate, :active)""")
        bind_param_st = statement.bindparams(tk=new_token, indate=indate, active=1)
        session.execute(bind_param_st, {"tk": new_token, "indate": indate, "active": 1})
        session.commit()
        # we close session
        session.close()
