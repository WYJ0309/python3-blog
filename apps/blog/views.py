from flask import render_template,request,session,redirect
from . import blogBlue


@blogBlue.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')
@blogBlue.route("/welcome",methods=["GET","POST"])
def welcome():

    return render_template("welcome.html")


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



@blogBlue.route("/demo/btn")
def btn():

    return render_template("/demo/btn.html")
@blogBlue.route("/demo/form")
def form():

    return render_template("/demo/form.html")
@blogBlue.route("/demo/table")
def table():

    return render_template("/demo/table.html")
@blogBlue.route("/demo/tab_card")
def tab_card():

    return render_template("/demo/tab_card.html")
@blogBlue.route("/demo/progress_bar")
def progress_bar():

    return render_template("/demo/progress_bar.html")
@blogBlue.route("/demo/folding_panel")
def folding_panel():

    return render_template("/demo/folding_panel.html")
@blogBlue.route("/demo/auxiliar")
def auxiliar():

    return render_template("/demo/auxiliar.html")
@blogBlue.route("/demo/add_edit")
def add_edit():

    return render_template("/demo/add_edit.html")
@blogBlue.route("/demo/data_table")
def data_table():

    return render_template("/demo/data_table.html")