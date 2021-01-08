# Python Program to perform Vertical Concat on String Array
from itertools import zip_longest

test_list = [["Gfg", "good"], ["is", "for"], ["Best"]]


concated = [
    "".join(x)
    for x in zip_longest(*test_list, fillvalue="")
]

print(concated)
