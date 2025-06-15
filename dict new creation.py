d={}
while True:
    n=input("enter name")
    k=input("enter value")
    d[n]=k
    ch=input("wish to continue y/n")
    if ch=="n" or ch=="N":
        break
print(d)
while True:
    e=input("enter name")
    if e in d:
        print("enter another name")
    else:
        s=input("enter details")
        d[e]=s
    ch=input("wish to continue y/n")
    if ch=="n" or ch=="N":
        break

print(d)
