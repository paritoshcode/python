s=input("enter string")
c=input("enter character")
for i in s:
    if i==c:
        print("found")
        break
else:
    print("not found")
