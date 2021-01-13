# Add tuples

def add_common_tuples():
    test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
    temp_dict = {elem: [] for elem, x in test_list}
    for elem in test_list:
        elem_key = temp_dict.get(elem[0], [])
        elem_key.append(elem[1])
    return [
        (key, *values) for key, values in temp_dict.items()
    ]


if __name__ == "__main__":
    print(add_common_tuples())
