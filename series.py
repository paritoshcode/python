n=int(input("enter number"))
s=1
for i in range(1,n+1):
    s=s+3
print(s)

n=int(input("enter number"))
x=int(input("enter number"))
s=0
for i in range(n+1):
    j=x**i
    s=s+1/j
print(s)
