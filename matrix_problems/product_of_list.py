# A Python Program to create the product of a list
from math import prod

test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

print(prod(
    [
        prod(x)
        for x in test_list
    ]
))

print(prod(
    [
        elem
        for sub in test_list
        for elem in sub
    ]
))
