l=[]
for i in l:
    a=int(input("enter number to add in in thw list"))
    s=input("what do you want to do y/n")
    if s=="n" or s=="N":
        break
    else:
        l.append(a)
print(l)
