import math

from flask import render_template, request, redirect, url_for
import dao
from saleapp import app, login
from flask_login import login_user, logout_user

@app.route('/login')
def form_login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/logout')
def logoutuser():
    logout_user()
    return redirect(url_for('signup'))

@app.route('/login', methods = ['POST', "GET"])
def login():

    if request.method == "POST":
        username = request.form.get('username')
        passw = request.form.get('passw')
        user = dao.check_login(username, passw)
        if user:
            login_user(user)
            return redirect(url_for('index'))
        else:
            error_mess = "Tên Đăng nhập và mật khẩu không chính xác!"
            return render_template('login.html', error_mess= error_mess)

    return redirect(url_for('index'))

@app.route('/logout' ,methods = ['GET', 'POST'])
def logout():
    if request.method.__eq__("POST"):
        pswd = request.form.get('pswd')
        pswd_repeat = request.form.get('pswd_repeat')

        if pswd.__eq__(pswd_repeat):
            data = request.form.copy()
            del data['pswd_repeat']

            avatar = request.files.get('avatar')
            dao.add_user(avatar=avatar, **data)
        else:
            error_mess = 'Mật khẩu không khớp!'

    return render_template('signup.html', error_mess=error_mess)



# @app.route('/login', method = ["POST", "GET" ] )
# def login():
#
#     return redirect(url_for('form_login'))


@app.route("/")
def index():


    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')

    page = request.args.get('page', 1)

    prods = dao.load_products(cate_id=cate_id, kw=kw, page = int(page))

    pages = math.ceil(dao.Cnt_Products() / app.config["PAGE_SIZE"])
    print(pages)

    return render_template("index.html", products=prods, pages =pages)


@app.context_processor
def comm_respone():
    return {

        'categories':  dao.load_categories()
    }


@login.user_loader
def user_load(id):
    return dao.get_user_by_id(id)

if __name__ == '__main__':
    app.run(debug=True)
