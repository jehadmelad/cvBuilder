from asyncio import tasks
from csv import unregister_dialect
from datetime import date, datetime
import email
from email.policy import default
from enum import unique
from telnetlib import STATUS
from xml.sax.handler import feature_namespace_prefixes
from . import db

from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id              = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.String(5) )
    fname           = db.Column(db.String(150) )
    lname           = db.Column(db.String(150) )
    email           = db.Column(db.String(150), unique=True)
    password        = db.Column(db.String(150) )
    avatar          = db.Column(db.String(200) )
    cv              = db.relationship('Cv')



class Cv(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    user_id         = db.Column(db.Integer, db.ForeignKey('user.id'))
    experience      = db.relationship('Experience')
    education       = db.relationship('Education')
    hardSkill       = db.relationship('HardSkill')
    details         = db.relationship('Details')
    social          = db.relationship('Social')
    project         = db.relationship('Project')
    language        = db.relationship('Language')

class Education(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    course          = db.Column(db.String(150) )
    university      = db.Column(db.String(150) )
    country         = db.Column(db.String(150) )
    degree          = db.Column(db.String(150) )
    discipline      = db.Column(db.String(150) )
    start_dt        = db.Column(db.DateTime, default=datetime.utcnow)
    end_dt          = db.Column(db.DateTime, default=datetime.utcnow)
    currently       = db.Column(db.Boolean(), default=False, nullable=True)
    description     = db.Column(db.String(150) )
    cv_id           = db.Column(db.Integer, db.ForeignKey('cv.id'))


class Experience(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    position        = db.Column(db.String(5) )
    company         = db.Column(db.String(150) )
    location        = db.Column(db.String(150) )
    start_dt        = db.Column(db.DateTime, default=datetime.utcnow)
    end_dt          = db.Column(db.DateTime, default=datetime.utcnow)
    currently       = db.Column(db.Boolean(), default=False, nullable=True)
    description     = db.Column(db.String(500) )
    cv_id           = db.Column(db.Integer, db.ForeignKey('cv.id'))
    

class Project(db.Model):
    id             = db.Column(db.Integer, primary_key=True)
    name           = db.Column(db.String(5) )
    place          = db.Column(db.String(150) )
    start_dt       = db.Column(db.DateTime, default=datetime.utcnow)
    end_dt         = db.Column(db.DateTime, default=datetime.utcnow)
    description    = db.Column(db.String(500) )
    cv_id          = db.Column(db.Integer, db.ForeignKey('cv.id'))



class HardSkill(db.Model):
    id             = db.Column(db.Integer, primary_key=True)
    name           = db.Column(db.String(5) )
    level          = db.Column(db.Integer )
    cv_id          = db.Column(db.Integer, db.ForeignKey('cv.id'))

class Details(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.String(5) )
    fname           = db.Column(db.String(150) )
    lname           = db.Column(db.String(150) )
    img             = db.Column(db.Text , unique=True, nullable= False )
    email           = db.Column(db.String(150), unique=True)
    address         = db.Column(db.String(150) )
    country         = db.Column(db.String(150) )
    city            = db.Column(db.String(150) )
    phone           = db.Column(db.String(150) )
    cv_id           = db.Column(db.Integer, db.ForeignKey('cv.id'))


class Social(db.Model):
    id             = db.Column(db.Integer, primary_key=True)
    name           = db.Column(db.String(150) )
    link           = db.Column(db.String(300) )
    cv_id          = db.Column(db.Integer, db.ForeignKey('cv.id'))
    

class Language(db.Model):
    id             = db.Column(db.Integer, primary_key=True)
    lang           = db.Column(db.String(5) )
    level          = db.Column(db.Integer)
    cv_id          = db.Column(db.Integer, db.ForeignKey('cv.id'))

