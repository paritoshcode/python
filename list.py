l=[]
s=0
while True:
    n=int(input("enter elements to add in list"))
    l.append(n)
    ch=input("do you wish to continue y/n")
    if ch=="n"or ch=="N":
         break
while True:
    print("enter what do you want to do 1. print list 2.sum of list 3.max element 4 min element 5. list in assending order 6. list in decending order ")
    g=int(input("enter number"))
    mx=mn=l[0]
    pmx=pmi=0
    if g==1:
        print(l)
    if g==2:
        for i in l:
            s=s+i
        print("sum",s)
    if g==3:
        for i in range(1,len(l)):
            if l[i]>mx:
                mx=l[i]
                pmx=i+1
        print("max element is", mx,"at position",pmx)
    if g==4:
        for i in range(1,len(l)):
            if l[i]<mn:
                mn=l[i]
                pmi=i+1
        print("max element is", mn,"at position",pmi)
    if g==5:
        for i in range(len(l)):
            for j in range(len(l)-1-i):
                if l[j]>l[j+1]:
                     l[j+1],l[j]=l[j],l[j+1]
        print(l)
    if g==6:
        for i in range(len(l)):
            for j in range(len(l)-1-i):
                if l[j]<l[j+1]:
                     l[j+1],l[j]=l[j],l[j+1]
        print(l)
