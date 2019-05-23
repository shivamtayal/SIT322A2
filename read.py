import pyodbc
import os
import re

server = '322-a2.database.windows.net'
dbname = 'mapreduce'
user = 'shivam'
passWord = 'tayal@123'



conn  = pyodbc.connect(
        "Driver={SQL Server};Server=322-a2.database.windows.net,1433;",
        user=user,password=passWord,database=dbname
)


def read():
    global conn
    cursor = conn.cursor()
    cursor.execute("SELECT * from Data")
    row = cursor.fetchone()
    total_rows = 0
    print("String,  Values")
    while (row):
        print (str(total_rows+1)+",  "+str(row[0])+",  "+str(row[1]))
        total_rows+=1
        row = cursor.fetchone()
    print("#################")
    print("Total Rows in Data = "+str(total_rows))


    

read()
