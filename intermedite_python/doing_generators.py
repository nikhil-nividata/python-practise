def evens(n):
    x = 2
    while x < n:
        yield x
        x += 2


# for u in evens(10):
#     print(u)

# for x in (2 * n for n in range(1, 10)):
#     print(x)
