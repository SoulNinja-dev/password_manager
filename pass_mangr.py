import mysql.connector
import os
db = mysql.connector.connect(
    host="localhost",
    user="soulninja",
    password="password17",
    database="password_manager"
)

cursor = db.cursor()

name = input("Enter your name: ")
print("Got it "+name)

def login():
    
    qry="SELECT name FROM main WHERE name=%s"
    cursor.execute(qry, (name,))

    isUser=cursor.fetchone()

    if isUser == None:
        print("You might wanna sign up")
    else:
        print("You're in boss")

login()
# CREATE TABLE main(
#    -> id INT AUTO_INCREMENT,
#    -> name VARCHAR(100),
#    -> website VARCHAR(255),
#    -> password VARCHAR(255),
#    -> PRIMARY KEY(id)

# 1. Check if user is new or old.
# if old then ask for password and check.
# if new then setup.

# 2. Options to put new password, show passwords, or change master password.

# 3. Create a table for each user.

