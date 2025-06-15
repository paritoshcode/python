import pymysql
try:
    db=pymysql.connect(host="localhost",user="root",password="paritosh",db="bookstore")
    print("SUCCESSFULLY CONNECTED")
except:
    print("database connection error")
def insert(sno,stname,price,quantity,tp):
    cur=db.cursor()
    q="insert into stationary values({},'{}',{},{},{})".format(sno,stname,price,quantity,tp)
    cur.execute(q)
    db.commit()
def delete(no):
    
    cur=db.cursor()
    q="delete from stationary where sno={}".format(no)
    cur.execute(q)
    db.commit()
def searchrecord(sno):
    cur=db.cursor()
    q="select * from stationary where sno={}".format(sno)
    cur.execute(q)
    x=cur.fetchall()
    if cur.rowcount>0:
        print("record found")
        for i in x :
            print("sno",i[0],"stname",i[1],"price",i[2],"quantity",i[3],"tp",i[4])
    else:
        print("record not found")
def display():
    cur=db.cursor()
    q="select * from stationary"
    cur.execute(q)
    x=cur.fetchall()
    if cur.rowcount>0:
        for i in x:
            print("sno",i[0],"stname",i[1],"price",i[2],"quantity",i[3],"tp",i[4])
    else:
        print("not found")
while True:
    print("1 insert")
    print("2 delete")
    print("3 search")
    print("4 display")
    ch=int(input("enter operation"))
    if ch==1:
        sno=int(input("enter sno "))
        stname=input("enter stname")
        price=int(input("price"))
        quantity=int(input("enter quantity"))
        tp=int(quantity*price)
        insert(sno,stname,price,quantity,tp)
        print("added")
    elif ch==2:
        sno=int(input("enter sno"))
        delete(sno)
        print("deleted")
    elif ch==3:
        sno=int(input("enter sno"))
        print(searchrecord(sno))
        print("ddone")
    elif ch==4:
        print(display())
    else:
        print("invalid operator")
        break
