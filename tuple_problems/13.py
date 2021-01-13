# Nested tuple into custom dictionary

def convert():
    test_tuple = ((1, 'Gfg', 2), (3, 'best', 4))
    keys = ['key', 'value', 'id']
    return [
        {
            k: val
            for k, val in zip(keys, elem)
        }
        for elem in test_tuple
    ]


if __name__ == "__main__":
    print(convert())
