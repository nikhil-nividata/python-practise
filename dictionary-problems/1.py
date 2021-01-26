def extract_unique():
    '''Function to extract unque values from dictionary'''
    test_dict = {
        'gfg': [5, 6, 7, 8],
        'is': [10, 11, 7, 5],
        'best': [6, 12, 10, 8],
        'for': [1, 2, 5]
    }
    return list(sorted({
        element
        for i_list in test_dict.values()
        for element in i_list
    }))


def extract_unique_chain():
    """Same function with Chain()"""
    from itertools import chain
    test_dict = {
        'gfg': [5, 6, 7, 8],
        'is': [10, 11, 7, 5],
        'best': [6, 12, 10, 8],
        'for': [1, 2, 5]
    }
    return list(sorted(set(chain(*test_dict.values()))))


if __name__ == "__main__":
    print(extract_unique())
    print(extract_unique_chain())
