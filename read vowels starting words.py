def addvowel():
    f=open("story.txt","r")
    f1=open("new.txt","w+")
    s=f.read().split()
    for i in s:
        if i[0] in "aeiouAEIOU":
            f1.write(i)
    print("record added")
    f.close()
    f1.close()
addvowel()
