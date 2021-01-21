number1 = int(input('Enter a first number: '))
number2 = int(input('Enter a second number: '))
number3 = int(input('Enter a third number: '))
operation = input('Enter operation [max, min, avg] ')
result = False

if operation == "max":
    largest_number = number1
    if number2 > largest_number:
        largest_number = number2
    if number3 > largest_number:
        largest_number = number3
    result = largest_number
elif operation == "min":
    smallest_number = number1
    if number2 < smallest_number:
        smallest_number = number2
    if number3 < smallest_number:
        smallest_number = number3
    result = smallest_number
elif operation == "avg":
    result = (number1 + number2 + number3) / 3

else:
    print(f"Error: unknown operation symbol: {operation}")

if result:
    print(f"Result: {result}")
