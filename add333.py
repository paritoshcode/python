import pickle
def add():
    f=open("story.dat","wb")
    
    while True:
        a=int(input("enter num"))
        na=input("enter name")
        Class=input("enter class")
        l=[a,na,Class]
        ch=input("enter choice")
        pickle.dump(l,f)

        if ch=="n":
            break
    
    f.close()
add()
