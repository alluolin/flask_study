from flask import Blueprint, url_for, redirect, render_template, request, make_response, abort, session

blue = Blueprint('xx',__name__)

@blue.route('/myblue')
def hello_blue_print():
    return '蓝图，规划URL'

@blue.route('/param/<id>')
def params(id):
    print(id)
    print((type(id)))
    return id

@blue.route('/params/<path:my_path>')
def param_path(my_path):
    print(my_path)
    import uuid
    uuid_val = uuid.uuid4()
    return uuid_val

@blue.route('/param_uuid/<uuid:my_uuid>')
def param_uuid(my_uuid):
    print(my_uuid)
    return "ok"

@blue.route('/my_any/<any(a,b,c):p>',methods=['GET','POST'])
def my_any(p):
    print(p)
    # res = url_for("xx.hello_blue_print")
    res = url_for('xx.params',id=1)

    return redirect(res)
@blue.route('/index')
def index():
    return render_template('one.html')

@blue.route('/req')
def look_req():
    req = request
    # print('req',req)
    # print('url',req.url)
    # print('path',req.path)
    # print('method',req.method)
    # # print(req.methods)
    # print('args',req.args)
    # print('form',req.form)
    print('file',req.files)
    print('file',req.files.getlist(''))
    print('file',req.files.get(''))
    print('ip',req.remote_addr)
    print('user',req.remote_user)
    print(dir(req.remote_user))
    return 'ok'

@blue.route('/response')
def my_response():
    # response = make_response('hehe',404)
    # response = make_response('hehe',500)
    abort(403)
    return 'hehe'

@blue.errorhandler(403)
def handle_403(e):
    return '无权限'

@blue.route('/home')
def home():

    uname = request.cookies.get('uname')
    # session_name = session.get('uname')
    uname=uname if uname else '游客'
    return render_template('home.html',uname=uname)

@blue.route('/login',methods=['POST','GET'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        uname = request.form.get('uname')
        response = redirect(url_for('xx.home'))
        response.set_cookie('uname',uname,max_age=30)
        # session['uname']=uname
        return response

    else:
        abort(405)


@blue.route('/logout',methods=['POST','GET'])
def logout():
    response = redirect(url_for('xx.home'))
    # session.pop('uname')
    response.delete_cookie('uname')

    return response



