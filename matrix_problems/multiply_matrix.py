# A Python Program to Multiply Matrices

X = [
    [1, 7, 3],
    [3, 5, 6],
    [6, 8, 9]
]

Y = [
    [1, 1, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]
]

result = [
    [
        sum(
            [
                X[i][k] * Y[k][j]
                for k in range(len(X[0]))
            ]
        )

        for j in range(len(Y[0]))
    ]
    for i in range(len(X))
]

for r in result:
    print(r)


res = [
    [
        sum([
            x*y for x, y in zip(x_row, y_col)
        ])
        for y_col in zip(*Y)
    ]
    for x_row in X
]

for r in res:
    print(r)
