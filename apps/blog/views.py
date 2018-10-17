from flask import render_template,request,session,redirect,url_for
from sqlalchemy import *
from ..models import Member
from apps import db,md5
from . import blogBlue


@blogBlue.route('/', methods=['GET', 'POST'])
@blogBlue.route('/index', methods=['GET', 'POST'])
def index():
    if session.get("user",None) is None:
        return redirect(url_for("blog.login"))

    #test_member = Member( "test1", md5("123456".encode("utf-8")), "13713464411")
    #db.session.add(test_member)
    #db.session.commit()
    return render_template('index.html')
@blogBlue.route("/welcome",methods=["GET","POST"])
def welcome():

    return render_template("welcome.html")

@blogBlue.route("/login",methods=["GET","POST"])
def login():
    msg = ''
    if request.method == 'POST':
        name = request.values.get('form-username')
        pwd = request.values.get('form-password')
        result = db.session.query(Member).filter_by(username=name).first()
        if result and md5(pwd.encode("utf-8")) == result.userpass:
            session['user'] = name  # 设置session的key value
            return redirect('/')
        else:
            msg = '用户名或者密码错误'
    else:
        if  'user' in session:
            return redirect(url_for("blog.index"))


    return render_template('login.html', msg=msg)

@blogBlue.route("/user_list",methods=["GET","POST"])
def user_list():
    username = request.args.get("username","")
    mobile = request.args.get("mobile","")
    current_page = request.args.get("current_page",1,type=int)  # 当前页数
    if current_page == 0:
        current_page = 1
    filter_str = ""
    if username != "":
        filter_str += Member.username.contains(username)+","
    if mobile != "":
        filter_str += Member.mobile.contains(mobile)+","


    pages = Member.query.filter(and_(filter_str)).paginate(current_page, 4, False)

    items = pages.items  # 获取查询的结果
    total_page = pages.pages  # 总页数
    args_str = ""
    for args_k in request.args:
        if current_page and args_k == "current_page":
            continue
        args_str += args_k+"="+request.args[args_k]+"&"
    args_str = args_str.strip("&")
    return render_template("user_list.html",**locals())