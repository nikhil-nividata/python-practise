# FLatten tuple of lists into a tuple

def flat_it():
    from itertools import chain
    test_tuple = ([5], [6], [3], [8])
    return tuple(chain.from_iterable(test_tuple))


if __name__ == "__main__":
    print(flat_it())
