from curses import flash
from dataclasses import dataclass
import datetime
from unicodedata import category
from flask import Blueprint ,render_template, redirect,request,url_for, flash
from flask_login import  current_user, login_required
from sqlalchemy import select, engine
from sqlalchemy.orm.session import Session
from .models import  User
# from . import db


views      = Blueprint("views", __name__)



@views.route('/', methods=['GET','POST'])
def home():

    return render_template("home.html", user = current_user)

@views.route('/delete/<int:id>')
def delete(id):
    

    return    redirect(url_for('views.home'))


@views.route('/complete/<int:id>', methods=['POST','GET'])
def complete(id):

    return  render_template('home.html' )
    

@views.route('/update/<int:id>', methods=['POST','GET'])
def update(id):

    return  render_template('home.html' )



@login_required #means do not show this page unless the user logged in.
@views.route('/buildResume', methods=['GET','POST'])
def buildResume():
        
    return  render_template('buildResume.html', user = current_user)

