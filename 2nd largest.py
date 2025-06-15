l=[]
while True:
    n=int(input("enter elements to add in list"))
    l.append(n)
    ch=input("wish to continue y/n")
    if ch=="n"or ch=="N":
        break
for i in range(len(l)):
            for j in range(len(l)-1-i):
                if l[j]<l[j+1]:
                    l[j+1],l[j]=l[j],l[j+1]
a=len(l)
if a==1:
    print(l[0])
else:    
    print(l[1])
