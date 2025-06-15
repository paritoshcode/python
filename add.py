def get_numbers_and_sum():
    d = []
    while True:
        a = int(input("Enter a number: "))
        ch = input("Do you want to enter another number? (y/n): ")
        if ch.lower() == "n":
            break
        else:
            d.append(a)
    
    # Calculate the sum of all elements in the list 'd' manually
    total_sum = 0
    for i in range( len(d)):
        total_sum += d[i]
    
    return total_sum

# Call the function to get numbers from the user and print the sum
result_sum = get_numbers_and_sum()
print("Sum of all elements entered:", result_sum)
