import datetime

# Define the subjects in the order of preference
subjects = ['Physics', 'Maths', 'Chemistry']

# Define the days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Define the number of hours for weekdays and weekend days
weekday_hours = 4
weekend_day_hours = 7

# Create a dictionary to store the time table
time_table = {day: [] for day in days}

# Create the time table
for day in days:
    if day in ['Saturday', 'Sunday']:
        hours = weekend_day_hours
    else:
        hours = weekday_hours
    for i in range(hours):
        if i < len(subjects):
            time_table[day].append(subjects[i])
        else:
            time_table[day].append('')

# Get the current day
current_day = datetime.datetime.now().strftime('%A')

# Define the current time
current_time = datetime.datetime.now().time()

# Calculate the total hours for the current day
if current_day in ['Saturday', 'Sunday']:
    total_hours = datetime.time(hour=23, minute=59, second=59)
else:
    print("no")
