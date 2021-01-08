import mysql.connector
import os
import time

# __init__
db = mysql.connector.connect(
    host="localhost",
    user="soulninja",
    password="password17",
    database="password_manager"
)

# global variables
cursor = db.cursor()
choice = 0

# methods


def choice():
    print("Hey, enter your choice: ")
    print('1. New User')
    print('2. Returning User')
    print('3. Exit')
    global choice
    choice = input()


def newUser():
    print('Hey enter your name: ')
    name = input()
    print('got it! now enter the website you want to store your password for')
    website = input()
    print('got that, now your secret password: ')
    password = input()
    cursor.execute(
        'INSERT INTO main (name,website,password) VALUES (%s,%s,%s)', (name, website, password))
    print('Yep got it! You can check back any time to retrieve your password')
    db.commit()


def oldUser():
    print('Welcome back, Please enter your name: ')
    name = input()
    print("Hey "+name+", choose an option you wanna see:")
    print("1. View Website and Password")
    print("2. Change website")
    print("3. Change password")
    print("4. Exit")
    choice = input()
    if choice == '1':
        cursor.execute(
            "SELECT website,password FROM main WHERE name=%s", (name,))
        for x in cursor:
            password = x
        print(password[0])
    if choice == '2':
        pass

        # main()
oldUser()


# comments for later reference


# def login():
# qry = "SELECT name FROM main WHERE name=%s"  # checking if user exists
#cursor.execute(qry, (name,))
#isUser = cursor.fetchone()
# global isNewUser
#  global isOldUser
#   if isUser == None:
#        isNewUser = 1
#        print('Hello there new user, Let me take you to sign up.././')
#    else:
#        isOldUser = 1
#        print('Hi there '+name+' Welcome back to password manager')
