d={}
while True:
    n=input("enter name")
    di=input("enter details")
    d[n]=di
    ch=input("wish to continue y/n")
    if ch=="n"or ch=="N":
        break
while True:
    print("what do you want to do 1.add a new element 2. display all elements 3. delete an element 4.update a value 5.search a particular name 6. exit")
    g=int(input("enter number"))
    if g==1:
        a=input("enter name")
        if a in d:
            print("enter another name")
        else:
            b=input("enter details")
            d[a]=b
            print(d)
    if g==2:
        print(d)
    if g==3:
        c=input("enter name")
        if c in d:
            del c[d]
            print("element",c,"is deleted and dict is",d)
        else:
            print("element not found")
    if g==4:
        e=input("enter name you want to edit")
        if e in d:
            f=input("enter details")
            d[e]=f
            print(d)
        else:
            print("name does not exist")
    if g==5:
        h=input("enter the name you want to search")
        if h in d:
            print("name found")
    if g==6:
        break
    
