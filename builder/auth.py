from flask import Blueprint, render_template, request, flash, redirect, url_for
import re

import sqlalchemy
from . import db
from .models import  User
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import MetaData, engine_from_config

from flask_login import login_required, login_user, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST','GET'])
def login():
    if request.method =="POST":
        email           = request.form.get("email")
        password        = request.form.get('1st-password')
        # print("#######################################################################################"+db.session.query(User))

        # try:
        user            = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("You are logged in. ", category="success")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Wrong password, try again.",category="warning")
        else:
            flash("You are not registred!!", category="warning") 
        # except sqlalchemy.exc.OperationalError as e:
            #    flash("You are not registred!!", category="warning") 
    return render_template("login.html",  user = current_user)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['POST','GET'])
def sign_up ():

    if request.method == "POST":
        if request.form['fname'] != "":
            fname           =   request.form.get('fname')
            lname           =   request.form.get('lname')
            email           =   request.form.get('email')
            password_1      =   request.form.get('1st-password')
            password_2      =   request.form.get('2nd-password')
            title           =   request.form.get('title')
            user            =   User.query.filter_by(email=email).first()

            if user:
                flash("This email already exist, try to login!!",category="warning")
            
            elif title == " ":
                flash("Please select a proper title (Mr/Mrs)!", category="error")
                return render_template("signup.html")
            # if len(fname) < 4 or type(fname) == "string" or CHARACTERS.isdigit(fname) == True:
            elif len(fname) < 3 or fname == " " or any(map(str.isdigit, fname)) == True :
                flash("A first name have to consist of 3 latter minimum!", category="error")
                return render_template("signup.html")

            elif len(lname) < 3 or lname == " " or any(map(str.isdigit, lname)) == True :
                flash("A last name have to consist of 3 latter minimum!", category="error")
                return render_template("/signup.html")

            elif len(email) < 6 or ( "@" in email) != True or ( "." in email) != True or email == " ":
                flash("Please enter a valid Email address!.", category="error")
                return render_template("signup.html")

            elif (len(password_1) < 8 
            or 
                re.search(r"\W", password_1) is  None or 
                re.search(r"\d", password_1) is  None or 
                re.search(r"[A-Z]", password_1) is  None or 
                re.search(r"[a-z]", password_1) is  None or password_1 == " "):         
                   
                flash("""An email have to consist of:   Length minmum: 8, 
                                                        At least 1 number, 
                                                        At least 1 capital latter, 
                                                        At least 1 small latter, 
                                                        At least 1 symbole.""" 
                                                        , category="error")
                return render_template("/signup.html")

            elif password_1 != password_2 :
                flash("Please confirm the passwords are same!", category="error")
                return render_template("/signup.html")

            else:
                new_user = User(fname=fname, lname=lname, title=title, email=email,password=generate_password_hash(password_1, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                flash("You have registred successfuly!",category="success")
                login_user(new_user, remember=True)
                return redirect(url_for("views.home"))
               
    return render_template("signup.html",  user = current_user)
