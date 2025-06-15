l=[1,2,3,4,5,6,7]
stack=[]
n=1
def push(st,n):
    for i in range(0,len(l),n):
        st.append(l[i])
l=[1,2,3,4,5,6,7]
n=1
print(push(l,n))
    
