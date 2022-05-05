from tkinter import *
from tkinter import messagebox
import os

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='itcompanies',
                                         user='root',
                                         password='Efgeghnlrtq@123')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)

cursor = connection.cursor()
result = cursor.execute('select * from service')
records = cursor.fetchall()
# for i in records:
#     print(i,"\n")
service = input("Tell the service required. If nothing press enter ")
if service == '':
    cname = input("Enter company name to see the services ")
    result = cursor.execute("select * from service where Cname = %s ",[cname])
    records = cursor.fetchall()
    print(f"Services provided by {cname} are: ")
    for i in records:
        print(i[1],"\n")
    pass 
else:
    result = cursor.execute("select * from service where Services like %s group by Cname",[service])
    records = cursor.fetchall()
    for i in records:
        print(i[0],"\n")


