
from api import Base, create_db_session
from sqlalchemy import Column, Integer, String, Boolean, DateTime

db_session = create_db_session()


class UrlTokens(Base):
    """UrlTokens table"""

    __tablename__ = 'urltokens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String(30), unique=False, nullable=False)
    insert_date = Column(DateTime, nullable=False)
    updated_date = Column(DateTime, nullable=False)
    is_active = Column(Boolean, nullable=False)

    def __init__(self, data):
        for key in data:
            setattr(self, key, data[key])

    def save_to_db(self):
        db_session.add(self)
        db_session.commit()

    @staticmethod
    def find_active_url_token():
        return db_session.query(UrlTokens).filter_by(is_active=True).one()
