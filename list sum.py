l=[]
s=0
while True:
    a=int(input("enter number"))
    l.append(a)
    ch=input("y/n")
    if ch=="n"or ch=="N":
        break
for i in l:
    s=s+i
print(s)
