d={}
s={}
while True:
    n=input("enter name")
    k=input("enter value")
    d[n]=k
    ch=input("wish to continue y/n")
    if ch=="n" or ch=="N":
        break
for i in range(len(d)):
    s=s+i
print(s)
