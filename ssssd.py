import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Function to clock in or out
def clock_in_out(employee_id, action):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open('attendance.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([employee_id, timestamp, action])

    messagebox.showinfo("Success", f'Employee {employee_id} has successfully {action} at {timestamp}')

# Function to display attendance data
def display_attendance_data():
    with open('attendance.csv', mode='r') as file:
        reader = csv.reader(file)
        attendance_data = "\n".join([", ".join(row) for row in reader])
        messagebox.showinfo("Attendance Data", f'Attendance Data:\n\n{attendance_data}')

# GUI Setup
def create_gui():
    root = tk.Tk()
    root.title("Employee Attendance Tracker")

    def clock_in():
        employee_id = entry_employee_id.get()
        clock_in_out(employee_id, 'clocked in')

    def clock_out():
        employee_id = entry_employee_id.get()
        clock_in_out(employee_id, 'clocked out')

    def show_attendance():
        display_attendance_data()

    label_employee_id = tk.Label(root, text="Employee ID:")
    label_employee_id.pack(pady=10)

    entry_employee_id = tk.Entry(root, width=30)
    entry_employee_id.pack()

    button_clock_in = tk.Button(root, text="Clock In", command=clock_in)
    button_clock_in.pack(pady=5)

    button_clock_out = tk.Button(root, text="Clock Out", command=clock_out)
    button_clock_out.pack(pady=5)

    button_show_attendance = tk.Button(root, text="Show Attendance Data", command=show_attendance)
    button_show_attendance.pack(pady=10)

    root.mainloop()

# Main function to handle user input
def main():
    create_gui()

if __name__ == "__main__":
    main()
