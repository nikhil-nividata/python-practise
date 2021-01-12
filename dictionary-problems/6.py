# Merging two dictionaries

def merge_with_chain():
    from itertools import chain
    dict1 = {'a': 10, 'b': 8}
    dict2 = {'d': 6, 'c': 4}
    return {
        k: val
        for k, val in
        zip((chain(dict1.keys(), dict2.keys())),
            chain(dict1.values(), dict2.values()))
    }


def merging_with_kwargs_syntax():
    dict1 = {'a': 10, 'b': 8}
    dict2 = {'d': 6, 'c': 4}
    return {
        **dict1,
        **dict2
    }


if __name__ == "__main__":
    print(merge_with_chain())
    print(merging_with_kwargs_syntax())
