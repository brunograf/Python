import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    database="testedb",
    user="root",
    password="1341408544"
)

mycursor = conn.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS testedb")
mycursor.execute("CREATE TABLE Members (MemberID int, LastName varchar(255))")