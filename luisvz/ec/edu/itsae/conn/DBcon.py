# coding:utf-8
'''
Created on 15/2/2015

@author: PC06
'''
from flaskext.mysql import MySQL
from flask import Flask
class DBcon():
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    pass

    def connexion(self):
        mysql = MySQL()
        app = Flask(__name__)
        app.config['MYSQL_DATABASE_USER'] = 'python'
        app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
        app.config['MYSQL_DATABASE_DB'] = 'ventas'
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        mysql.init_app(app)
        return mysql


'''
con=DBcon().connexion().connect().cursor()
sql="select * from personas"
con.execute(sql)
row=con.fetchall()
for x in row:
    print (x)  

'''