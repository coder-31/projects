import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='')
cur=con.cursor()

def create_db():
    cur.execute("create database if not exists PHONES")
    print("database created successfully")

def open_db():   
    query="use PHONES"
    cur.execute(query)
    print("database opened successfully")

def create_table():
    query="create table if not exists smrt(srno integer primary key,smrtnm varchar(30),ram integer, rom char,price integer(10))"
    cur.execute(query)
    print("smrt table created successfully")

def create_records(srno,smrtnm,ram,rom,price):
    query="insert into smrt values(%s,'%s',%s,'%s',%s)" % (srno,smrtnm,ram,rom,price)
    cur.execute(query)
    con.commit()
    print("new smrt record inserted successfully")

def show_data():
    query="select * from smrt"
    cur.execute(query)
    l=cur.fetchall()
    from tabulate import tabulate
    print(tabulate(l,headers=['srno','smrtnm','ram','rom','price'],tablefmt='psql'))

    
def search_no(srno):
    '''Function to search and display the record of a smartphone from smrt table by serial number'''
    query="select * from smrt where srno=%s" % (srno,)
    cur.execute(query)
    l=cur.fetchall()
    
    if l==[]:
        print(srno,"smartphone not found")
        return
    print("Record details of smartphone:",srno)
    try:
        for rec in l:
            print(rec[0],rec[1],rec[2],rec[3],rec[4])
    except:
        print("Invalid details of smartphone")
        
def search_name(smrtnm):
    '''Function to search and display the record of an smartphone from smrt table by smartphone name'''
    query="select * from smrt where smrtnm='%s'" % (smrtnm,)
    cur.execute(query)
    l=cur.fetchall()
    if l==[]:
        print(smrtnm,"smartphone not found")
        return
    
    print("Record details of smartphone with name:",smrtnm)
    try:
        for rec in l:
            print(rec[0],rec[1],rec[2],rec[3],rec[4])
    except:
        print("Record not found!")

def update_record(srno):
    '''Function to search for and edit smartphone
    name,ram,price as per user requirement'''
    query="select * from smrt where srno=%s" % (srno,)
    cur.execute(query)
    l=cur.fetchall()
    if l==[]:
        print(smrtnm,"smartphone not found")
        return
    try:
        print("Record to be updated with serial number",srno,"found")
        print(l)
        rec=list(l[0])
        print("serial number",srno,"record before updation:")
        print(rec)

        ch=input("Update name [y/n]?")
        if ch.upper()=='Y':
            rec[1]=input("Enter the new name:")

        ch=input("Update ram [y/n]?")
        if ch.upper()=='Y':
            rec[2]=int(input("Enter the new ram:"))

        ch=input("Update price [y/n]?")
        if ch.upper()=='Y':
            rec[4]=int(input("Enter the new price:"))
    
        query="update smrt set smrtnm= '%s',ram=%s,rom='%s',price= %s where srno=%s" % (rec[1],rec[2],rec[3],rec[4],srno)
        cur.execute(query)
        con.commit()
        print("Record has been updated")
    except:
        print("Invalid serial number")

def delete_record(srno):
    '''Function to search for and delete a record
    of an smartphone from smrt table
    as per the serial number passed to it'''
    query="select * from smrt where smrtno=%s" % (smrtno,)
    cur.execute(query)
    l=cur.fetchall()
    if l==[]:
        print(srno,"smartphone not found")
        return
    print(srno,"found")
    
    rec=list(l[0])
    print("smartphone",srno,"record before deletion:")
    print(rec)

    ch=input("Confirm deletion [y/n]?")
    if ch.upper()=='Y':
        cur.execute("delete from smrt where srno=%s" % (srno,))
        con.commit()
    print("Table after record deletion:")
    show_data()

def close_db():
    cur.close()
    con.close()
    print("Connection to database closed...")
    
def menu():
    while True:
        print("1. Show table")
        print("2. create record")
        print("3. Search by serial number")
        print("4. Search by mobile  name")
        print("5. Update record")
        print("6. Delete record")
        print("7. Close database")
        ch=int(input("Enter your choice:"))
        if ch==1:
            show_data()
        elif ch==2:
            srno=int(input("Enter serial number: "))
            smrtnm=str(input("Enter mobile name: "))
            ram=int(input("Enter mobile ram: "))
            rom=str(input("Enter rom: "))
            price=int(input("Enter smartphone price: "))
            create_records(srno,smrtnm,ram,rom,price)
        elif ch==3:
            srno=int(input("Enter serial number: "))
            search_no(srno)
        elif ch==4:
            smrtnm=str(input("Enter mobile name: "))
            search_name(smrtnm)
        elif ch==5:
            empno=int(input("Enter serial number: "))
            update_record(srno)
        elif ch==6:
            empno=int(input("Enter serial number: "))
            delete_record(srno)
        elif ch==7:
            close_db()
            break
    
        else:
            print("wrong input")


create_db()
open_db()
create_table()
menu()




