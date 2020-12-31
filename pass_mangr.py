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
isNewUser=0
isOldUser=0
# methods 

def signup():
    print('Welcome, Hope you like your stay here at password manager,')
    print('We keep all your passwords safe and secure! ')
    print('Please enter your name again')
    global name
    input(name)


def login():
    
    qry="SELECT name FROM main WHERE name=%s"  # checking if user exists
    cursor.execute(qry, (name,))

    isUser=cursor.fetchone()
    global isNewUser 
    global isOldUser
    if isUser == None:
        isNewUser = 1
        print('Hello there new user, Let me take you to sign up.././')
    else:
        isOldUser = 1
        print('Hi there '+name+' Welcome back to password manager')
# main() 
login()

if(isNewUser==1):
    signup()
else:
    print('So what u wanna do today')





# CREATE TABLE main(
#    -> id INT AUTO_INCREMENT,
#    -> name VARCHAR(100),
#    -> website VARCHAR(255),
#    -> password VARCHAR(255),
#    -> PRIMARY KEY(id)



# 1. make sign up method which will allow the user to sign up.

# 2. Options to put new password, show passwords, or change master password.

# 3. Create a table for each user.

