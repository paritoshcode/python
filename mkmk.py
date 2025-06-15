import csv
def CreateCSV1():
    Csvfile=open('student.csv','w', newline='') 
    Csvobj =csv.writer(Csvfile)
    while True:
        Rno =int(input("Rollno:"))
        Name =input("Name:")
        Marks=float(input("Marks:"))
        Line=[Rno,Name,Marks]
        Csvobj.writerow(Line) 
        Ch=input("More(Y/N)?")
        if Ch=='N':
            break
    Csvfile.close() 
CreateCSV1()
