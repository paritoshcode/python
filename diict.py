d={}
while True:
    k=input("Enter the name")
    n=input("Enter all the details")
    d[k]=n
    ch=input("Y or N")
    if ch=="N" or ch=="n":
        break
while True:
    print("1-add new elemnt, 2- display all elements, 3-delete an element in a dictionary , 4-update a value,5-search a particular name,6-exit")
    g=int(input("Enter the n."))
    if g==1:
        kk=input("Enter name")
        if kk in d:
            print("Give another name")
        else:
            nn=input("Enter detail")
            d[kk]=nn
    if g==2:
        print(d)
    if g==3:
        b=input("Enter the element name")
        if b in d:
            del d[b]
        else:
            print("Name does not exist")
    if g==4:
        pp=input("Enter the name you want to edit")
        if pp in d :
            cc=input("Enter the details")
            d[pp]=cc
        else:
            print("Name does not exist")
    if g==5:
        gg=input("Enter the name")
        if gg in d:
            print("found")
    if g==6:
        break
