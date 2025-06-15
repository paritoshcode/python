import pickle
def print():
    f=open("story.dat","rb")
    while True:
        s=pickle.load(f)
        print(s)
    f.close()
print()
