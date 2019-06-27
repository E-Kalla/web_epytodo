from app import app
import cgi
from flask import render_template
from flask import Flask, request
import sqlite3
import mysql.connector

@app.route('/user/', methods =['GET'])
@app.route('/user', methods =['GET'])
def     user():
            return ("User")
@app.route('/signout/', methods =['GET','POST'])
@app.route('/signout', methods =['GET','POST'])
def     signout():
            return ("Logout")
@app.route('/signin/', methods =['POST','GET'])
@app.route('/signin', methods =['POST','GET'])
def     signin():
        if request.method == 'GET':
            return render_template("login.html")
        else :
            connexion = mysql.connector.connect(host="127.0.0.1",user="route",password="123",database="epytodo")
            cursor = connexion.cursor()
            username = request.form['user']
            password = request.form['password']
            cursor.execute("SELECT * FROM user WHERE username = '%s'" % (username))
            if len (cursor.fetchall()) == 0 :
                cursor.close()
                connexion.close()
                return render_template("login.html", error="error: username doesn't exist")
            cursor.execute("SELECT password FROM user WHERE username = '%s'" % (username))
            realpassword = cursor.fetchone()[0]
            if realpassword != password :
                    return render_template("login.html", error="error: username and password doesn't match")
            else :
                return render_template("login.html",error="signin successful")
@app.route('/register/', methods =['POST','GET'])
@app.route('/register', methods =['POST','GET'])
def     register():
        if request.method == 'GET':
            return render_template("register.html")
        else :
            connexion = mysql.connector.connect(host="127.0.0.1",user="route",password="123",database="epytodo")
            cursor = connexion.cursor()
            username = request.form['user']
            password = request.form['password']
            cursor.execute("SELECT * FROM user WHERE username = '%s'" % (username))
            if len (cursor.fetchall()) != 0 :
                cursor.close()
                connexion.close()
                return render_template('register.html', error="error: account already exists")
            cursor.execute("INSERT INTO user (username,password) VALUES ('%s','%s')" % (username ,password))
            connexion.commit()
            cursor.close()
            connexion.close()
            return render_template('register.html', error="account created")
@app.route('/contact/',methods =['GET'])
@app.route('/contact',methods =['GET'])
def     contact():
        return render_template("contact.html")

@app.route('/task',methods =['GET','POST'])
@app.route('/task/',methods =['GET','POST'])
def     task():
    return render_template("task.html")

@app.route('/',methods =['GET'])
@app.route('/index', methods=['GET'])
def     route_home():
    return render_template("index.html")