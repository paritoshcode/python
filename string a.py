s=input("enter string")
q=0
w=0
e=0
r=0
while True:
    a=input("y/n")
    if a=="n"or a=="N":
        break
    else:
        for i in s:
            if i.isalpha():
                q=q+1
            elif i.isdigit():
                w=w+1
            elif i.isspace():
                e=e+1
            elif i.isspace():
                r=r+1
print(q,w,e,r)
        
