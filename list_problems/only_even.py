m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [x for x in filter(lambda x: x % 2 == 0, m)]

print(evens)
