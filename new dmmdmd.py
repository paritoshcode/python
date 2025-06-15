def create():
    try:
        f=open("w.txt","w")
        while True:
            s=input("enter line")
            f.write(s+"\n")
            ch=input("y/n")
            if ch.lower()=="n":
                break
        print("data added")
        f.close()
    except:
        print("file opening error")
create()
