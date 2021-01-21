number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
number3 = int(input('Enter the third number: '))
operation = input('Enter operation [max, min, avg] ')

if operation == "max":
    largest_number = number1
    if number2 > largest_number:
        largest_number = number2
    if number3 > largest_number:
        largest_number = number3
    print(f"Largest number: {largest_number}")
elif operation == "min":
    smallest_number = number1
    if number2 < smallest_number:
        smallest_number = number2
    if number3 < smallest_number:
        smallest_number = number3
    print(f"Smallest number: {smallest_number}")
elif operation == "avg":
    result = (number1 + number2 + number3) / 3
    print(f"Result: {result}")
else:
    print(f"Error: unknown operation symbol: {operation}")
