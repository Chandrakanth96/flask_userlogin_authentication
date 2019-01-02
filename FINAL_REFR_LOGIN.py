# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 00:34:22 2018

@author: Chandru
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 22:37:49 2018

@author: Chandru
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 07:53:09 2018

@author: Chandru
"""

from flask import Flask
from flask import render_template
from flask import request
import mysql.connector
from dbconfig import db, cursor
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('dumfun01@gmail.com','pythongurukula')

message = "Successfully Registered click on the Link 192.168.1.187/validate"

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registeruser')
def register():
	return render_template('register.html')

@app.route('/pushdatatodb',methods=['POST','GET'])
def pushdatatodb():
    print("Inside Push to DB")
    if request.method == 'POST':
        print("Inside Post")
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['inputEmail']
        mobileno = request.form['mobileno']
        password = request.form['inputPassword']
        print(firstname,lastname,email,mobileno,password)
        sql =("Select * from usermanagement ")
        #val = (firstname,email, )
        cursor.execute(sql)
		#cursor.execute('''INSERT INTO 'usermanagement' ('id', 'first_name', 'last_name', 'email', 'mobileno', 'temp_password', 'perm_password') VALUES ('1' %s, %s, %s, %s, %s, NULL),firstname,lastname,email,mobileno,password''')
		#db.commit()
        for res in cursor:
            #for i in res:
            #print(i)
            print(res[1],res[3])
            if res[1]==firstname and res[3]==email:
                return("SORRY Already Registered.. Try LOG IN ! ")
            
        sql = "INSERT INTO usermanagement (first_name, last_name, email, mobileno, temp_password) VALUES (%s, %s, %s, %s, %s)"
        val = (firstname, lastname, email, mobileno, password)
        cursor.execute(sql, val)
        db.commit()
        server.sendmail('dumfun01@gmail.com',email,message)
        server.quit()
        return "You're Registration is Successful Check your Inbox to Verify"
		         
@app.route('/validate')
def validate():
    return render_template('login_validate.html')

@app.route('/validateuser',methods=['POST','GET'])
def checklogin_validate():
    #print("hello user")
    if request.method == 'POST':
        email = request.form['inputEmail']
        password = request.form['inputPassword']
        #print(email,password)
        sql = ("SELECT * FROM usermanagement WHERE email = %s")
        val = (email, )
        
        cursor.execute(sql,val)
        for res in cursor:
            #print(res[3],res[5])
            if res[3]==email and res[5]==password:
               #print("Welcome")
               sql=("Update usermanagement set perm_password= %s where email=%s")
               val=(password,email, )
               cursor.execute(sql,val)
               db.commit()
               return ("Welcome: "+res[1]+" . "+res[2]+" ....You are Verified ..!")
            else:
                return("Invalid Email/Password Combination")
                
@app.route('/validatelogin',methods=['POST','GET'])
def checklogin():
    #print("hello user")
    if request.method == 'POST':
        email = request.form['inputEmail']
        password = request.form['inputPassword']
        #print(email,password)
        sql = ("SELECT * FROM usermanagement WHERE email = %s")
        val = (email, )
        
        cursor.execute(sql,val)
        for res in cursor:
           # print(res[3],res[5])
            
            if res[3]==email and res[6]==password:
               # print("Welcome")
               return ("Welcome: "+res[1]+" "+res[2])
            elif res[3]==email and res[5]==password:
                return("Please Check Your mail and Confirm Registration to Login")
            else:
                return("Invalid Email/Password Combination")           
        
if __name__ == '__main__':
	app.run(port=4500,debug=False)
