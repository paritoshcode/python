s=[]
while True:
    print("1.push 2pop 3display")
    c=int(input("enter operation(1,2,3)"))
    if c==1:
        n=input("enter what to add")
        s.append(n)
    elif c==2:
        if s==[]:
            print("under flow")
        else :
            print("delted element is",s.pop())
    elif c==3:
        
        print(s[::-1])
    ch=input("y/n")
    if ch=="n":
        break
    
