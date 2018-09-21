from flask import render_template
from . import blogBlue



@blogBlue.route('/', methods=['GET', 'POST'])
def base():

    return render_template('base.html',title="这个是基础页面")

@blogBlue.route("/register",methods=["GET","POST"])
def register():
    context = {
        'username': "王亚锋",
        'age': "18",
        'gender': "男",
        'flag': "王者",
        'hero': "猴子",
        'wwwurl': {
            'baidu': 'www.baidu.com',
            'google': 'www.google.com'
        }
    }

    #传递指定的字典或变量给模板
    return render_template("register.html", **context)

@blogBlue.route("/login",methods=["GET","POST"])
def login():

    #传递所有的函数内变量给模板
    return  render_template("login.html", **locals())