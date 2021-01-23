"""Вывести на экран фигуры, заполненные звездочками. Диалог с
 пользователем реализовать при помощи меню:
 a             b                 c             d              e
 * * * * *     *             * * * * *                    * * * * *
   * * * *     * *             * * *                        * * *
     * * *     * * *             *             *              *
       * *     * * * *                       * * *          * * *
         *     * * * * *                   * * * * *      * * * * *
"""
operation = input("Enter operation [a, b, c, d, e]: ")
if operation == "a":
    print(f'Figure # 1 \n')
    t = 0
    n = 11
    for i in range(11):
        t += 2
        n -= 1
        print('\n'.join([' ' * t + '* ' * n]))
elif operation == "b":
    print(f'Figure # 2\n')
    n = 1
    t = 0
    for i in range(11):
        t += 2
        print('\n'.join(['* ' * i + ' ' * t]))
    print('\n')
elif operation == "c":
    print(f'Figure # 3\n')
    n = 1
    t = 9
    print('* ' * 10)
    for i in range(6):
        n += 2
        t -= 2
        print('\n'.join([' ' * n + '* ' * t]))
elif operation == "d":
    print(f'Figure # 4\n')
    n = 1
    t = 10
    print(' ' * 10 + '* ')
    for i in range(11, 1, -3):
        n += 2
        t -= 2
        print('\n'.join([' ' * t + '* ' * n]))
    print('\n')
elif operation == "e":
    print(f'Figure # 5\n')

    n = 1
    t = 9
    print('* ' * 10)
    for i in range(3):
        n += 2
        t -= 2
        print('\n'.join([' ' * n + '* ' * t]))
    print(' ' * 9 + '* ' * 1)
    n = 1
    t = 9
    for i in range(4, 1, -1):
        n += 2
        t -= 2
        print('\n'.join([' ' * t + '* ' * n]))
    print('* ' * 10)
else:
    print(f"Error: unknown operation symbol: {operation}")
