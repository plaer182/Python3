"""
    Заполнить динамически Python репрезентацию шахматной доски в виде
    матрицы (двумерного листа). Черные клетки обозначить 1, белые 0.
"""

matrix_chess = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

for i in range(0, 8, 2):
    for j in range(len(matrix_chess[i])):
        if j % 2 != 0:
            matrix_chess[i][j] = 1
for i in range(1, 8, 2):
    for j in range(len(matrix_chess[i])):
        if j % 2 == 0:
            matrix_chess[i][j] = 1

for row in matrix_chess:
    print(row)
