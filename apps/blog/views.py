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


    pages = Member.query.filter(and_(filter_str)).order_by(desc("id")).paginate(current_page, 4, False)

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

    return render_template("user_add.html", **locals())

@blogBlue.route("/user_post",methods=["GET","POST"])
@login_required
def user_post():
    if request.method == "POST":
        user_id = request.form.get("user_id")
        if user_id is None:
            formData = request.form
            jsonDict = {
                "username": formData["username"],
                "userpass": md5(formData["userpass"].encode("utf-8")),
                "mobile": formData["mobile"],
                "nickname": formData["nickname"],
                "nation": formData["nation"],
                "birth_day": formData["birth_day"],
                "motto": formData["motto"],
                "resume": formData["resume"],
                "address": formData["address"]
            }
            #test_member = Member(formData["username"],formData["userpass"],formData["nickname"],formData["nation"],formData["birth_day"],formData["motto"],formData["mobile"],formData["address"],formData["resume"])
            test_member = Member(**jsonDict)
            db.session.add(test_member)
            db.session.commit()
        else:
            formData = request.form
            jsonDict = {
                "username": formData["username"],
                "mobile": formData["mobile"],
                "nickname": formData["nickname"],
                "nation": formData["nation"],
                "birth_day": formData["birth_day"],
                "motto": formData["motto"],
                "resume": formData["resume"],
                "address": formData["address"]
            }
            if formData["userpass"].strip() != "":
                jsonDict["userpass"] = md5(formData["userpass"].encode("utf-8"))
            Member.query.filter_by(id=user_id).update(jsonDict)
            db.session.commit()
        data = {
            'status': 'ok',
            'code': 200,
            'msg': "操作成功"
        }
        json_str = json.dumps(data, ensure_ascii=False)
        return json_str
    else:
        data = {
            'status': 'ok',
            'code': 200,
            'msg': "请求类型不正确"
        }
        json_str = json.dumps(data,ensure_ascii=False)
        return json_str

@blogBlue.route("/user_edit",methods=["GET","POST"])
@login_required
def user_edit():
    user_id = request.args.get("user_id")

    user = Member.query.filter_by(id=user_id).first()
    return render_template("user_edit.html", **locals())


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

@blogBlue.route("/user_del",methods=["GET","POST"])
@login_required
def user_del():
    user_id = request.args.get("user_id")

    Member.query.filter_by(id=user_id).delete()
    db.session.commit()
    data = {
        'status': 'ok',
        'code': 200,
        'msg': "操作成功"
    }
    json_str = json.dumps(data, ensure_ascii=False)
    return json_str