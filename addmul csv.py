import csv
def add():
    l=[]
    f=open("new1.csv","w",newline="")
    s=csv.writer(f)
    while True:
        k=[]
        n=int(input("enter numer"))
        na=input("enter author name")
        y=int(input("enter year"))
        p=int(input("price"))
        k=[n,na,y,p]
        l.append(k)
        ch=input("y/n")
        if ch=="n":
            break
    print(l)
    s.writerows(l)
    f.close()
add()
    
