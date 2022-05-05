from tkinter import *
from tkinter import messagebox
import os

import mysql.connector
from mysql.connector import Error

def register():
    global service,cname
    global u_entry,p_entry,root1,root
    global root,screen_w,screen_h,x,y
    root=Tk()
    screen_w=root.winfo_screenwidth()
    screen_h=root.winfo_screenheight()
    x=screen_w/2.7
    y=screen_h/2.7
    root = Tk()
    root1=Toplevel(root)
    service = StringVar()
    cname = StringVar()
    root1.title("Display Page")
    root1.configure(bg="#F1C40F")
    w1=350
    h1=310
    root1.geometry("%dx%d+%d+%d" %(w1,h1,x,y))
    Label(root1,text="Please enter the company name\nin the given empty fields",font=("Georgia",15),bg="#F9E79F").pack()
    Label(root1,text="",bg="#F1C40F").pack()
    Label(root1,text="Company Name *",font=("Georgia",15),bg="#F9E79F").pack()
    Label(root1,text="",bg="#F1C40F").pack()
    u_entry=Entry(root1,textvariable=cname,width="15",borderwidth=3)
    u_entry.pack()
    Label(root1,text="",bg="#F1C40F").pack()
    Label(root1,text="Service Required *",font=("Georgia",15),bg="#F9E79F").pack()
    Label(root1,text="",bg="#F1C40F").pack()
    p_entry=Entry(root1,textvariable=service,width="15",borderwidth=3)
    p_entry.pack()
    Label(root1,text="",bg="#F1C40F").pack()
    button=Button(root1,text="Continue",width=10,command=test(service,cname),bg="#F9E79F",font=("Georgia",12)).pack()
    # root1.mainloop()
    # return service,cname

def test():
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
    service,cname = register()
    if service == '':
        cname = input("Enter company name to see the services ")
        result = cursor.execute("select * from service where Cname = %s ",[cname])
        records = cursor.fetchall()
        print("Services provided by {cname} are: ")
        for i in records:
            print(i[1],"\n")
        pass 
    else:
        result = cursor.execute("select * from service where Services like %s group by Cname",[service])
        records = cursor.fetchall()
        for i in records:
            print(i[0],"\n")

register()