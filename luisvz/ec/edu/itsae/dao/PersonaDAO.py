# coding:utf-8
'''
Created on 18/1/2015

@author: Usuario
'''

from ec.edu.itsae.conn import DBcon
import json


class PersonaDAO(DBcon.DBcon):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
        
    def repotarPersona(self):
        con=self.connexion().connect().cursor()
        sql="select * from personas"
        con.execute(sql)
        row=con.fetchall()
        return row
    
    def insertarPersona(self, nombre, apaterno, amaterno, dni, fnacimiento, sexo, direccion, celular, estado):
        con=self.connexion().connect()
        sql="""insert into personas (nombre, apell_paterno, apell_materno, dni, fecha_nacimiento, sexo, direccion, celular, estado)
                values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %i)
                """ %(nombre, apaterno, amaterno, dni, fnacimiento, sexo, direccion, celular, estado)
                
        print sql
        with con:
            cursor=con.cursor()
            cursor.execute(sql)
            
    def login(self, usuario, clave):
        con=self.connexion().connect().cursor()
        sql="select * from trabajador where usuario='%s' and clave='%s'" %(usuario,clave)
        con.execute(sql)
        row=con.fetchall()
        return row
    
    def buscarPersonaNombre(self, datobuscado):
        con=self.connexion().connect().cursor()
        con.execute("""select CONCAT(nombre,' ', apell_paterno,' ', apell_materno)as value, idpersona as id from personas where upper (CONCAT(nombre,' ', apell_paterno,' ', apell_materno)) like upper('%s')""" %("%" + datobuscado + "%"))
        reporte=con.fetchall()
        columna=('value','id')
        lista=[]
        
        for row in reporte:
            lista.append(dict(zip(columna,row)))
        return json.dumps(lista, indent=2)
    
    
    def buscarPersonaDato(self, datobuscado):
        con=self.connexion().connect().cursor()
        sql="""select * from personas where upper (CONCAT(nombre,' ', apell_paterno,' ', apell_materno)) like upper('%s')""" %("%" + datobuscado + "%")
        con.execute(sql)
        reporte=con.fetchall()
        return reporte
    