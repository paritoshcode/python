def countthe():
    with open("story.txt","r")as f:
        f1=open("sms.txt","w")
        c=f.read()
        s=0
        for i in c:
            if i =="the":
                s=+1
            print(s)
        f1.close()
countthe()
