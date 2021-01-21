number1 = int(input('Enter a first number: '))
number2 = int(input('Enter a second number: '))
operation = input('Enter operation [a, b, c, d] ')
count = 0


if operation == "a":
    for i in range(number1, number2 + 1):
        print(i)

elif operation == "b":
    for i in range(number2, number1 - 1, -1):
        print(i)

elif operation == "c":
    for i in range(number1, number2 + 1):
        if i % 7 == 0:
            print(i)

elif operation == "d":
    for i in range(number1, number2 + 1):
        if i % 5 == 0:
            count += 1
    print(count)

else:
    print(f"Error: unknown operation symbol: {operation}")
