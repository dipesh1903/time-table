import MySQLdb
import numpy as np


y = np.zeros((5,8,4) , dtype = int)
db = MySQLdb.connect("localhost","dipesh1903","12345","timedb")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS teacher")
cursor.execute("DROP TABLE IF EXISTS subject")
cursor.execute("DROP TABLE IF EXISTS teaching")
sql = """ create table teacher(
        tid INT AUTO_INCREMENT PRIMARY KEY,
	name varchar(50) not null,
	available int not null, days varchar(5) not null) """

sql1 = """ create table subject(sid INT AUTO_INCREMENT PRIMARY key,sub_name varchar(100) not null)""" 

sql2 = """create table teaching(lid INT AUTO_INCREMENT PRIMARY KEY , tid int not null , sid int not null , dept int not null , year int not null)"""
cursor.execute(sql)
cursor.execute(sql1)
cursor.execute(sql2)
db.close()
