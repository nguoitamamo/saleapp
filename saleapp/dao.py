import hashlib

from saleapp.models import Category, Product, User
from saleapp import app, db
import hashlib
import cloudinary

def load_categories():
    return Category.query.order_by("id").all()


def load_products(cate_id=None, kw=None, page =1):
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))

    if cate_id:
        query = query.filter(Product.category_id == cate_id)


    pagesize = app.config["PAGE_SIZE"]

    start = (page - 1 ) * pagesize
    end = start + pagesize



    return query.slice(start, end)


def Cnt_Products():
    return Category.query.count()



def get_user_by_id(id):
    return User.query.get(id)


def check_login(username , passw):
    passnew= str(hashlib.md5(passw.strip().encode('utf-8')).hexdigest())
    return User.query.filter( User.username.__eq__(username), User.passw.__eq__(passnew) ).frist()


def add_user(name, username , pswd , avatar = None):
    passnew = str(hashlib.md5(pswd.strip().encode('utf-8')).hexdigest())
    user = User( name= name, username = username.strip() , passw = passnew)

    if avatar:
        res = cloudinary.uploader.upload(avatar)
        user.avatar = res.get('secure_url')

    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        print(get_user_by_id('2'))