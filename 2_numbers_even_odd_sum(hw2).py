number1 = int(input('Enter a first number: '))
number2 = int(input('Enter a second number: '))
even = 0
odd = 0
s = 0
count1 = 0
count2 = 0
count3 = 0

if number1 <= 0:
    print("Error: invalid first number")
if number2 <= 0:
    print("Error: invalid second number")
if number1 > 0 and number2 > 0:
    for i in range(number1, number2 + 1):
        if i % 2 == 0:
            even += i
            count1 += 1
    print(even)
    for i in range(number1, number2 + 1):
        if i % 2 != 0:
            odd += i
            count2 += 1
    print(odd)
    for i in range(number1, number2 + 1):
        s += i
        count3 += 1
    print(s)
    print(even / count1)
    print(odd / count2)
    print(s / count3)
