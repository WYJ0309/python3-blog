from apps import db,login_manager
import time
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Member(UserMixin,db.Model):
    __tablename__ = 'cmf_member'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    nickname = db.Column(db.String(50))
    nation = db.Column(db.String(50))
    birth_day = db.Column(db.String(50))
    motto = db.Column(db.String(50))
    mobile = db.Column(db.String(12))
    address = db.Column(db.String(50))
    resume = db.Column(db.Text(5000))
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

    def __init__(self,username,userpass,nickname,nation,birth_day,motto,mobile,address,resume):
        self.username = username
        self.userpass = userpass
        self.nickname = nickname
        self.nation = nation
        self.birth_day = birth_day
        self.motto = motto
        self.mobile = mobile
        self.address = address
        self.resume = resume

    def __repr__(self):
        return '<Member: %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return Member.query.get(int(user_id))

class Role(db.Model):

    __tablename__ = "roles"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)
    # 给Role类创建一个uses属性，关联users表。
    # backref是反向的给User类创建一个role属性，关联roles表。这是flask特殊的属性。
    users = db.relationship('User',backref="role")
    # 相当于__str__方法。
    def __repr__(self):
        return "Role: %s %s" % (self.id,self.name)


class User(db.Model):
    # 给表重新定义一个名称，默认名称是类名的小写，比如该类默认的表名是user。
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)
    email = db.Column(db.String(32),unique=True)
    password = db.Column(db.String(40))
    # 创建一个外键，和django不一样。flask需要指定具体的字段创建外键，不能根据类名创建外键
    role_id = db.Column(db.Integer,db.ForeignKey("roles.id"))

    def __repr__(self):
        return "User: %s %s %s %s" % (self.id,self.name,self.password,self.role_id)
