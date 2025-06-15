l=[]
while True:
    n=int(input("enterb number"))
    l.append(n)
    print(l)
    ch=input("wish to continue y/n")
    if ch=="n"or ch=="N":
        break
print("entered list",l)
n=len(l)
if n%2==1:
    n=n-1
    for i in range(0,n-1):
        l[i],l[i+1]=l[i+1],l[i]
print(l)
