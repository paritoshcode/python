import pickle
def addrec():
    f=open("g.dat","wb")
    d={}
    while True:
        no=int(input("enter numer"))
        name=input("enter name")
        airline=input("enter name airline")
        d={"fno.":no,"fname":name,"airline":airline}
        pickle.dump(d,f)
        ch=input("enter operation")
        if ch=="n":
            break
    f.close()
addrec()
        
