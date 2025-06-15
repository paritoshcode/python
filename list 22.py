l=[]
while True:
    n=int(input("enter elements to add in list"))
    l.append(n)
    ch=input("wish to continue y/n")
    if ch=="n"or ch=="N":
        break
while True:
    print("what do you want to do 1.print list 2. sum of all elements 3.maximum number and its position 4. min and position 5. search element and position 6. assending order 7. decending order 9. exit")
    g=int(input("enter number"))
    if g==1:
        print(l)
    if g==2:
        s=0
        for i in l:
            s=s+i
        print(s)
    if g==3:
        mx=l[0]
        pmx=0
        for i in range(len(l)):
            if l[i] > mx:
                mx=l[i]
                pmx=i+1
        print(mx,"at",pmx)
    if g==4:
        mn=l[0]
        pmi=0
        for i in range(len(l)):
            if l[i]<mn:
                mn=l[i]
                pmi=i+1
        print(mn,"at",pmi)
    if g==5:
        s=int(input("enter element to search"))
        for i in range(len(l)):
            if l[i]==s:
                print("element",s,"is found at",i+1)
            else:
                print("element not found")
    if g==6:
        for i in range(len(l)):
            for j in range(len(l)-1-i):
                if l[j]<l[j+1]:
                    l[j+1],l[j]=l[j],l[j+1]
        print(l)
    if g==7:
        for i in range(len(l)):
            for j in range(len(l)-1-i):
                if l[j]>l[j+1]:
                    l[j+1],l[j]=l[j],l[j+1]
        print(l)
    if g==8:
        break
    
                    
            
