from flask import render_template,request,session,redirect
from . import blogBlue
from  apps import db

@blogBlue.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')
@blogBlue.route("/welcome",methods=["GET","POST"])
def welcome():

    render_template("welcome.html")





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
    msg = ''
    if request.method == 'POST':
        name = request.values.get('form-username')
        pwd = request.values.get('form-password')
        if name == 'wyj' and pwd == '123456':
            session['user'] = name  # 设置session的key value
            return redirect('/')
        else:
            msg = '用户名或者密码错误'
    return render_template('login.html', msg=msg)