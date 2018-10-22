from flask import render_template,request,session,redirect,url_for,flash,jsonify
from flask_login import login_required, login_user, logout_user
from sqlalchemy import *
from ..models import Member
from apps import db,md5
from . import blogBlue
import  json


@blogBlue.route('/', methods=['GET', 'POST'])
@blogBlue.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    if session.get("user",None) is None:
        return redirect(url_for("blog.login"))

    #test_member = Member( "test1", md5("123456".encode("utf-8")), "13713464411")
    #db.session.add(test_member)
    #db.session.commit()
    return render_template('index.html')

@blogBlue.route("/welcome",methods=["GET","POST"])
@login_required
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
            login_user(result, name)
            return redirect('/')
        else:
            msg = '用户名或者密码错误'
    else:
        if  'user' in session:
            return redirect(url_for("blog.index"))


    return render_template('login.html', msg=msg)

@blogBlue.route("/login_out")
@login_required
def login_out():

    session.pop("user")
    session.clear()
    logout_user()
    flash(u"登出账号成功")
    return redirect(url_for("blog.login"))

@blogBlue.route("/user_list",methods=["GET","POST"])
@login_required
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

@blogBlue.route("/user_add",methods=["GET","POST"])
@login_required
def user_add():

    if request.method == "POST":

        #{"price_min":"1","price_max":"1","quiz1":"浙江","quiz2":"杭州","quiz3":"余杭区","":"111","":"111111111111111","file":""}
        formData = request.form

        test_member = Member(formData["username"],formData["userpass"],formData["nickname"],formData["nation"],formData["birth_day"],formData["motto"],formData["mobile"],formData["address"],formData["resume"])
        db.session.add(test_member)
        db.session.commit()

        return redirect(url_for("blog.user_list",form_json=formData["username"]))
    else:
        return render_template("user_add.html",**locals())

@blogBlue.route("/img_upload",methods=["GET","POST"])
@login_required
def img_upload():
    if request.method == 'POST':
        f = request.files['file']
        filename = f.filename
        # f.save(os.path.join('app/static',filename))
        f.save('apps/static/images/user/' + str(filename))
        f_json = {
            "code":0,
            "msg":"上传成功",
            "data":{
                "src":'static/images/user/' + str(filename),
                "title":str(filename)
            }
        }
        return jsonify(f_json)
    else:
        return "not ok"