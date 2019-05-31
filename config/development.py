# -*- coding:utf-8 -*-
from configparser import ConfigParser

config = ConfigParser()
config.read("secret.ini")

SERVER_PORT = 8888  # 端口号
SERVER_HOST = '127.0.0.1'  # 访问地址
DEBUG = True  # 调试模式
RELEASE_VERSION = '1.0'  # 发布版本

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = config.get('DatabaseSecretKey', 'USERNAME')
PASSWORD = config.get('DatabaseSecretKey', 'PASSWORD')
HOST = config.get('DatabaseSecretKey', 'HOST')
PORT = config.get('DatabaseSecretKey', 'PORT')
DATABASE = config.get('DatabaseSecretKey', 'DATABASE')
SQLALCHEMY_ENCODING = 'utf-8'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
                                                          PORT, DATABASE)
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True

DOMAIN = "http://{}:{}".format(SERVER_HOST, SERVER_PORT)


WECHAT_APP = {
    'AppID': config.get('WX_APP', 'AppID'),
    'AppKey': config.get('WX_APP', 'AppKey')
}


WX_CONFIG = {
    'DOMAIN': DOMAIN,
    'STATIC': DOMAIN + '/static/uploadFile/',
    'ARTICLES_PAGE_SIZE': 10
}

EMAIL_CONFIG = {
    "mail_host": config.get('EmailSetting', 'mail_host'),
    "mail_port": config.get('EmailSetting', 'mail_port'),
    "mail_user": config.get('EmailSetting', 'mail_user'),
    "mail_pass": config.get('EmailSetting', 'mail_pass'),
    "sender": config.get('EmailSetting', 'sender'),
}
