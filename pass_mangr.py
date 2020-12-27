import mysql.connector
import os 
db = mysql.connector.connect(
        host="localhost",
        user="soulninja",
        password="password17",
        database="password_manager"
        )

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# mycursor.execute("INSERT Person (name, age) VALUES (%s,%s)", ("Tim", 19))

# db.commit()
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

os.system("clear")
print("clearing screen.... ")
print("Saved all right homie, you can leave now!")
print("See you soon")


