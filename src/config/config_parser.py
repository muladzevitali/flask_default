import configparser
import os
from dataclasses import dataclass

config = configparser.ConfigParser()
config.read("config.ini")
base_dir = os.path.abspath('.')

os.environ["NLS_LANG"] = "AMERICAN_AMERICA.AL32UTF8"


@dataclass(init=False)
class Oracle:
    """Configuration class for oracle databases"""
    database_user = config["ORACLE"]["USER"]
    database_password = config["ORACLE"]["PASSWORD"]
    database_name = config["ORACLE"]["DATABASE"]
    database_ip = config["ORACLE"]["IP"]
    database_port = config["ORACLE"]["PORT"]
    uri = "oracle+cx_oracle://%s:%s@%s:%s/%s" % (
        database_user, database_password,
        database_ip, database_port, database_name)


@dataclass(init=False)
class SqLite:
    uri = f'sqlite:///{base_dir}/media/database/development.db'


@dataclass(init=False)
class ApplicationDatabase:
    uri = SqLite.uri if config['DATABASE']['DATABASE'] == 'SQLITE' else Oracle.uri
    table_prefix = config['DATABASE']['TABLE_PREFIX']


@dataclass(init=False)
class Application:
    SECRET_KEY = config["APPLICATION"]["SECRET_KEY"]
    WTF_CSRF_SECRET_KEY = config['APPLICATION']['WTF_CSRF_SECRET_KEY']
    SECURITY_USER_IDENTITY_ATTRIBUTES = 'username'
    FLASK_ADMIN_SWATCH = "lumen"
    SQLALCHEMY_ECHO = config["APPLICATION"]["SQLALCHEMY_ECHO"] == "true"
    SQLALCHEMY_TRACK_MODIFICATIONS = config["APPLICATION"]["SQLALCHEMY_TRACK_MODIFICATIONS"] == "true"
    SQLALCHEMY_DATABASE_URI = ApplicationDatabase.uri

    @staticmethod
    def init_app(app):
        pass


@dataclass()
class Media:
    media_path = config["FILES"]["MEDIA_PATH"]
    log_file_info = config["LOGGER"]["LOG_FILE_INFO"]
    log_file_error = config["LOGGER"]["LOG_FILE_ERROR"]

    def __init__(self):
        os.makedirs(self.media_path, exist_ok=True)


@dataclass(init=False)
class Mail:
    host = config["MAIL"]["HOST"]
    port = config["MAIL"]["PORT"]
    sender = config["MAIL"]["FROM"]


@dataclass(init=False)
class LDAP:
    email = config['LDAP']['EMAIL']
    password = config['LDAP']['PASSWORD']
