from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
import os,hashlib


config_name = os.getenv("FLASK_CONFIG") or "default"
app = Flask(__name__)
app.config.from_object(config[config_name])
app.debug = True
config[config_name].init_app(app)
db = SQLAlchemy()
db.init_app(app)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'blog.login'
login_manager.init_app(app)
def md5(temp):
    # 首先是获取要加密的字符串的长度
    new_temp = temp[0:len(temp) - 1]
    # 创建md5对象
    m = hashlib.md5()
    # 生成加密字符串
    m.update(new_temp)
    # 获取加密后的字符串
    sign = m.hexdigest()
    return sign

from . blog import blogBlue
app.register_blueprint(blogBlue)