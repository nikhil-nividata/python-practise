X = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Y = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]


def add_matrix(a, b):
    result = []
    for i in range(len(a)):
        n = []
        for j in range(len(a[i])):
            n.append(a[i][j] + b[i][j])
        result.append(n)
    return result


print(add_matrix(X, Y))

result = [
    [
        X[i][j] + Y[i][j]
        for j in range(len(X[0]))
    ] for i in range(len(X))
]

print(result)
