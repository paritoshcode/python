
STUDENT = {"Alice": 50, "Bob": 20, "Charlie": 70, "David": 45, "Eve": 28}

STUD = []


for name, mark in STUDENT.items():

    if mark < 33:
        STUD.append(name)

print("STUDENT dictionary:", STUDENT)
print("Students with marks less than 33:", STUD)
