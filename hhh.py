import csv
from datetime import datetime

# Function to clock in or out
def clock_in_out(employee_id, action):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open('attendance.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([employee_id, timestamp, action])

    print(f'Employee {employee_id} has successfully {action} at {timestamp}')

# Function to display attendance data
def display_attendance_data():
    with open('attendance.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Main function to handle user input
def main():
    while True:
        print("\nEmployee Attendance Tracker")
        print("1. Clock In")
        print("2. Clock Out")
        print("3. Display Attendance Data")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            employee_id = input("Enter Employee ID: ")
            clock_in_out(employee_id, 'clocked in')
        
        elif choice == '2':
            employee_id = input("Enter Employee ID: ")
            clock_in_out(employee_id, 'clocked out')
        
        elif choice == '3':
            print("\nAttendance Data:")
            display_attendance_data()
        
        elif choice == '4':
            print("Exiting the program...")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
