l=[]
while True:
    n=int(input("enterb number"))
    l.append(n)
    print(l)
    ch=input("wish to continue y/n")
    if ch=="n"or ch=="N":
        break
print("entered list",l)
for i in range(len(l)):
    for j in range(len(l)-1-i):
        if l[j]>l[j+1]:
            l[j+1],l[j]=l[j],l[j+1]
print(l)
