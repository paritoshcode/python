f=open("story.txt",'w')
while True:
    s=input("Enter a line:")
    f.write(s+"\n")
    ch=input("Wish to continue? n/y:")
    if ch.lower()=='n':
        break
    print("Data Added.")

except:
print("File opening error")
f.close()
