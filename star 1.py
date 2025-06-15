while True:
    print("1st,2nd,3,4,5,6,7")
    n=int(input("enter operation"))
    if n==1:
        for i in range(5):
            for j in range(i+1):
                print(i,end="")
            print()
    if n==2:
        for i in range(5):
            for k in range(4-i):
                print(" ",end="")
            for j in range(i+1):
                print(i,end="")
            print()
    if n==3:
        for i in range(5):
            for k in range(4-i):
                print(" ",end="")
            for j in range(i+1+i):
                print(i,end="")
            print()
    if n==4:
        for i in range(4,-1,-1):
            for k in range(4-i):
                print(" ",end="")
            for j in range(i+1+i):
                print(i,end="")
            print()
    if n==5:
        for i in range(5):
            for k in range(4-i):
                print(" ",end="")
            for j in range(i+1+i):
                print(i,end="")
            print()

        for i in range(3,-1,-1):
            for k in range(4-i):
                print(" ",end="")
            for j in range(i+1+i):
                print(i,end="")
            print()            
        
    if n==7:
        print("exiting")
        break
