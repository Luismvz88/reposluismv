'''
Created on 18/1/2015

@author: Usuario
'''

from app import app
from flask import redirect,url_for, request
from ec.edu.itsae.dao import PersonaDAO
from flask.templating import render_template



@app.route("/add")
def foradd():
    nombre=request.args.get("nombre")
    apellpaterno=request.args.get("apellpaterno")
    apellmaterno=request.args.get("apellmaterno")
    dni=request.args.get("dni")
    fecha=request.args.get("fecha")
    sexo=request.args.get("sexo")
    direccion=request.args.get("direccion")
    celular=request.args.get("celular")
    estado=int(request.args.get("estado"))
    PersonaDAO.PersonaDAO().insertarPersona(nombre, apellpaterno, apellmaterno, dni, fecha, sexo, direccion, celular, estado)
    
    return redirect(url_for("index"))


@app.route("/add2", methods=['POST'])
def foradd2():
    nombre=request.form.get('nombre',type=str)
    apellpaterno=request.form.get('apellpaterno',type=str)
    apellmaterno=request.form.get('apellmaterno',type=str)
    dni=request.form.get('dni',type=str)
    fecha=request.form.get('fecha',type=str)
    sexo=request.form.get('sexo',type=str)
    direccion=request.form.get('direccion',type=str)
    celular=request.form.get('celular',type=str)
    estado=request.form.get('estado',type=int)
    PersonaDAO.PersonaDAO().insertarPersona(nombre, apellpaterno, apellmaterno, dni, fecha, sexo, direccion, celular, estado)
    
    return redirect(url_for("index"))



@app.route("/validar")
def validar():
    usuario=request.args.get("username")
    clave=request.args.get("password")
    x=PersonaDAO.PersonaDAO().login(usuario, clave)
    if len(x)==1:
        return redirect(url_for("index"))
    else:
        return redirect(url_for("login"))
    
    
    
@app.route("/buscarauto")
def buscarPersonaAuto():
    nombre=str(request.args.get('term'))
    objR=PersonaDAO.PersonaDAO().buscarPersonaNombre(nombre)
    return objR



@app.route("/buscarDato")
def buscarPersonaDato():
    nombre=str(request.args.get('bnombre'))
    objR=PersonaDAO.PersonaDAO().buscarPersonaDato(nombre)
    return render_template("index.html",dato=objR)
    