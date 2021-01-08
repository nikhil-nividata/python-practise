test_list = [
    [4, 5, 6],
    [8, 1, 10],
    [7, 12, 5]
]


def get_k_column(matrix, k):
    return [
        row[k]
        for row in matrix
    ]


print(get_k_column(test_list, 0))
print(get_k_column(test_list, 1))
print(get_k_column(test_list, 2))


def get_k_column_zip(matrix, k):
    return zip(*matrix)[k]


print(get_k_column_zip(test_list, 0))
print(get_k_column_zip(test_list, 1))
print(get_k_column_zip(test_list, 2))
