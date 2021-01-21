number = int(input('Enter the number: '))

if 0 <= number <= 100:
    if number % 15 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
elif number < 0:
    print("Error: unknown symbol")
else:
    print("Error: unknown symbol")
