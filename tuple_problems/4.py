# Add Tuple to list and list to tuple

def tup_plus_list():
    test_list = [5, 6, 7]
    test_tup = (9, 10)
    from itertools import chain
    return tuple(chain(test_tup, test_list))


def list_plus_tuple():
    test_list = [5, 6, 7]
    test_tup = (9, 10)
    test_list.extend(test_tup)
    return test_list


if __name__ == "__main__":
    print(tup_plus_list())
    print(list_plus_tuple())
