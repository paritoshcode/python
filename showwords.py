def show_words():
    f=open("story.txt","r")
    c=f.read()
    for i in c:
        print(i.upper(),end="")
    f.close()
show_words()
