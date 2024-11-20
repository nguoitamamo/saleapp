from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary

app = Flask(__name__)
app.config["SECRET_KEY"] = "âssdadadads"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saleapp?charset=utf8mb4" % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 8


db = SQLAlchemy(app)


login = LoginManager(app)


cloudinary.config(
    cloud_name = "ddkpaw2gy",
    api_key = "622254564989568",
    api_secret = "wAoO0Elvy5y-SWqpsjQNw43PRt0", # Click 'View API Keys' above to copy your API secret
    secure=True
)