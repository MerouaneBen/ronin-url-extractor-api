# some  static variables
import os


class Config(object):
    SECRET_KEY = os.getenv('SECRET')
    API_PORT = os.getenv('API_PORT')
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + os.getenv('MYSQL_USER')+ ":" + os.getenv('MYSQL_PASSWORD') + "@" + os.getenv('MYSQL_HOST') + ":" + os.getenv('MYSQL_PORT') + "/" + Config.MYSQL_DATABASE + "?charset=utf8mb4"
