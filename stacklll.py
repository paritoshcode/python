def popon(novel):
    if novel==[]:
        print("underflow")
    else:
        print("deleted novel",novel.pop())
a=eval(input("enter list"))
popon(a)
print(a)
