import mysql.connector
import os 
db = mysql.connector.connect(
        host="localhost",
        user="soulninja",
        password="password17",
        database="password_manager"
        )

mycursor = db.cursor()

# CREATE TABLE main(
#    -> id INT AUTO_INCREMENT,
#    -> name VARCHAR(100),
#    -> website VARCHAR(255),
#    -> password VARCHAR(255),
#    -> PRIMARY KEY(id)
#    -> );

name = input("Hey welcome, Whats your good name? ") 
print("Sounds good ",name)
website = input("Now which website do you want to save your password in? ")
print("Gotcha")
password = input("now the password.. ")

mycursor.execute("INSERT main (name,website,password) VALUES (%s,%s,%s)", (name, website, password))
db.commit()



def welcome():
    name = input("Hey wassup, what's your good name?")
    try:
    


os.system("clear")
print("clearing screen.... ")
print("Saved all right homie, you can leave now!")
print("See you soon")

# 1. Check if user is new or old.
    # if old then ask for password and check.
    # if new then setup.

# 2. Options to put new password, show passwords, or change master password.

# 3. Create a table for each user.

