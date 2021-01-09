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
cursor = db.cursor()

# methods


def main():
    print("Hey, enter your choice: ")
    print('1. New User')
    print('2. Returning User')
    print('3. Exit')
    choice = input()
    print('----------------~---------------')
    if choice == '1':
        newUser()
    if choice == '2':
        oldUser()
    if choice == '3':
        exit()


def newUser():
    print('Hey enter your name: ')
    name = input()
    print('')
    print('Got it! now enter the website you want to store your password for')
    website = input()
    print('')
    print('Got that, now your secret password: ')
    password = input()
    print('')
    cursor.execute(
        'INSERT INTO main (name,website,password) VALUES (%s,%s,%s)', (name, website, password))
    print('Yep got it! You can check back any time to retrieve your password')
    db.commit()
    print('----------------~---------------')
    time.sleep(2)


def oldUser():
    print('----------------~---------------')
    print('Welcome back, Please enter your name: ')
    name = input()
    print('')
    print("Hey "+name+", choose an option you wanna see:")
    print("1. View Website and Password")
    print("2. Change website")
    print("3. Change password")
    print("4. Exit")
    choice = input()
    print('----------------~---------------')
    password = '', ''
    if choice == '1':
        cursor.execute(
            "SELECT website,password FROM main WHERE name=%s", (name,))
        for x in cursor:
            password = x
        print('website: ' + password[0])
        print('password: ' + password[1])
        print('----------------~---------------')
    if choice == '2':
        print('New Website name: ')
        newWebsiteName = input()
        cursor.execute(
            'UPDATE main SET website=%s WHERE name=%s', (newWebsiteName, name,))
        db.commit()
        print('Changed...')
        print('----------------~---------------')
    if choice == '3':
        print('Enter your new secure password: ')
        newPassword = input()
        cursor.execute(
            'UPDATE main SET password=%s WHERE name=%s', (newPassword, name,))
        db.commit()
        print('Changed...')
        print('')
    if choice == '4':
        exit()
    time.sleep(2)


# main()
while True:
    main()
