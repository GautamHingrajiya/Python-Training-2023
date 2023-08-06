import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="")

mycursor = mydb.cursor()

# create database in mysql

mycursor.execute("CREATE DATABASE IF NOT EXISTS 15JUN_CRUD")
mydb.commit() # save and execute

mydb = pymysql.connect(host="localhost",user="root",password="",database="15JUN_CRUD")
mycursor=mydb.cursor()

# create table inside database

mycursor.execute("CREATE TABLE IF NOT EXISTS STUDENT( id int primary key auto_increment , name varchar(20), subject varchar(20), city varchar(20) )")
mydb.commit()