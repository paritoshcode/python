def factorial():
    f=open("story.txt","r")
    f1=open("digits.txt","w")
    c=f.read()
    for i in c:
        if i.isdigit():
            f1.write(i)
factorial()
