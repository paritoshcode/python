import csv
def add():
    f=open("new.csv","w",newline="")
    s=csv.writer(f)
    n=int(input("enter numer"))
    na=input("enter author name")
    y=int(input("enter year"))
    p=int(input("price"))
    l=[n,na,y,p]
    s.writerow(l)
    f.close()
add()
