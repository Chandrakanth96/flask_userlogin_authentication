import mysql.connector
db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='chandru',
        port=6033)
cursor = db.cursor()
cursor.execute('''CREATE database managedb''')
cursor.execute('''CREATE TABLE managedb.usermanagement ( id INT(5) NOT NULL AUTO_INCREMENT , first_name VARCHAR(40) NOT NULL , last_name VARCHAR(40) NOT NULL , email VARCHAR(50) NOT NULL , mobileno VARCHAR(20) NOT NULL , temp_password VARCHAR(50) NOT NULL , perm_password VARCHAR(50) NULL , PRIMARY KEY (id)) ''')


