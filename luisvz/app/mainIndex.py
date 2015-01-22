# coding:utf-8
'''
Created on 18/1/2015

@author: Usuario
'''
from app import app
from flask.templating import render_template
from ec.edu.itsae.dao import PersonaDAO

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/persona")
def index():
    x=PersonaDAO.PersonaDAO().repotarPersona()
    return render_template("index.html",dato=x)