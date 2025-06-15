a=0
b=1
print(a,b,end=",")
for i in range(10):
    a,b=b,a+b
    print(b,end=",")
