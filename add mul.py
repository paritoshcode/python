def add():
    f=open("story.txt","w")
    while True:
        s=input("enter to add in txt")
        f.write(s)
        ch=input("enter operation y/n")
        if ch=="n":
            break
    f.close()
add()
