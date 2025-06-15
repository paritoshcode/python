l=[]
while True:
    n=int(input("enterb number"))
    l.append(n)
    print(l)
    ch=input("wish to continue y/n")
    if ch=="n"or ch=="N":
        break
s=int(input("enter the number to check weather prime or not"))
for i in range(1,s):
    if s%i==0:
        print("its not prime")
    elif s==0:
        print("not defined")
    else:
        print(s,"is prime number")
