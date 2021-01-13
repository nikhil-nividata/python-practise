# Get k max min

def get_it():
    test_tup = (5, 20, 3, 7, 6, 8)
    sortx = sorted(test_tup)
    x = 2
    from itertools import chain
    return list(
        chain(sortx[:x], sortx[-x:])
    )


if __name__ == "__main__":
    print(get_it())
