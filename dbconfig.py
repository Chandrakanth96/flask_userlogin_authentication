import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',password='chandru',port=6033,database='managedb')
cursor = db.cursor()

