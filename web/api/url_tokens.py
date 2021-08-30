
from api import db



class UrlTokens(db.Model):
    """UrlTokens table"""

    __tablename__ = 'urltokens'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(30), unique=False, nullable=False)
    insert_date = db.Column(db.DateTime, nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True)
    is_active = db.Column(db.Boolean, nullable=False)

    def __init__(self, token, insert_date, updated_date,is_active):
        self.token = token
        self.insert_date = insert_date
        self.updated_date = updated_date
        self.is_active = is_active
