def sumlist(lst):
    t = 0
    for i in range(len(lst)):
        t += l[i]
    return t

# Function to get list of integers from user input
def b():
    l = []
    while True:
        a = input("Enter a number (or enter any non-numeric value to stop): ")
        if a.isdigit():
            num = int(a)
            l.append(num)
        else:
            break
    return l

# Example usage:
print("Enter numbers to calculate their sum (enter any non-numeric value to stop):")
user_list = b()
result_sum = sumlist(user_list)
print("Sum of all elements in the list:", result_sum)
