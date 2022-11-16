from os import path
from wsgiref.util import request_uri
from flask import Flask 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)

    #in production never share this key
    app.config['SECRET_KEY'] = "shoul not be shared"
    #website_url = 'demo.jehadmelad.tech'
    #app.config['SERVER_NAME'] = website_url

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from .views import views
    from .auth import auth


    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")


    from .models import User

    

#  New version of sqlalcheny has changed by using this way instead of:
#       
#   create_db(app)
# 
# check if there is a bd within the folder.
# def create_db(app):
#     if not path.exists('tracker/'+DB_NAME):
#         db.create_all()
    with app.app_context():
        db.create_all()
        # print("Database  ( "+ DB_NAME +" ) successfuly created!")
        

    login_manager                =   LoginManager()
    login_manager.login_view     = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def  load_user(id):
        return User.query.get(int(id))



    return app

