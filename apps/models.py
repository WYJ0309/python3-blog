from apps import db
import time
from werkzeug.security import generate_password_hash, check_password_hash

class Member(db.Model):
    __tablename__ = 'cmf_member'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    mobile = db.Column(db.String(12))
    userpass = db.Column(db.String,default="123456")
    add_time = db.Column(db.Integer,default=int(time.time()))

    @property
    def password(self):
        return self.userpass

    # 定义一个赋值的方法
    @password.setter
    def password(self, pwd):
        self.userpass = generate_password_hash(pwd)

    def check_password(self, pwd):

        return check_password_hash(self.userpass, pwd)

    def __init__(self,username,pwd,mobile):
        self.username = username
        self.userpass = pwd
        self.mobile = mobile

    def __repr__(self):
        return '<Member %r>' % self.username
