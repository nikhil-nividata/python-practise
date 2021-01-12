# Append in Order

def do_it():
    test_dict = {"Gfg": 1, "is": 2, "Best": 3}
    from itertools import chain
    return list(chain(test_dict.keys(), test_dict.values()))


if __name__ == "__main__":
    print(do_it())
