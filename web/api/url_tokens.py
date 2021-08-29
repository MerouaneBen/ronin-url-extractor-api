
from api import db



class UrlTokens(db.Model):
    """UrlTokens table"""

    __tablename__ = 'urltokens'
    id = Column(db.Integer, primary_key=True, autoincrement=True)
    token = Column(db.String(30), unique=False, nullable=False)
    insert_date = Column(db.DateTime, nullable=False)
    updated_date = Column(db.DateTime, nullable=False)
    is_active = Column(db.Boolean, nullable=False)

    def __init__(self, token, insert_date, updated_date,is_active):
        self.token = token
        self.insert_date = insert_date
        self.updated_date = updated_date
        self.is_active = is_active
