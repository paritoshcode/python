import csv
def display():
    f=open("new1.csv","r")
    s=csv.reader(f)
    for i in s:
        print(i)
    f.close()
display()
