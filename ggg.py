import csv
from datetime import datetime

def clock_in_out(employee, action):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open('attendance.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([employee, timestamp, action])

    print(f'Employee {employee} has successfully {action} at {timestamp}')

def attendance():
    with open('attendance.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def search_attendance(employee):
    found = False
    with open('attendance.csv', mode='r') as file:
        reader = csv.reader(file)
        print(f"\nAttendance records for Employee ID {employee}:")
        for row in reader:
            if row[0] == employee:
                print(row)
                found = True
    if not found:
        print(f"No attendance records found for Employee ID {employee}.")

def main():
    while True:
        print("\nEmployee Attendance Tracker")
        print("1. Clock In")
        print("2. Clock Out")
        print("3. Display Attendance Data")
        print("4. Search Attendance by Employee ID")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            employee = input("Enter Employee ID: ")
            clock_in_out(employee, 'clocked in')
        
        elif choice == '2':
            employee = input("Enter Employee ID: ")
            clock_in_out(employee, 'clocked out')
        
        elif choice == '3':
            print("\nAttendance Data:")
            attendance()
        
        elif choice == '4':
            employee = input("Enter Employee ID to search: ")
            search_attendance(employee)
        
        elif choice == '5':
            print("Exiting the program...")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
