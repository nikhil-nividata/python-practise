# Remap the values

def remap():
    from itertools import chain
    test_dict = {"gfg": [1, 2, 3], "is": [1, 4], "best": [4, 2]}
    new_dict = dict.fromkeys(chain(*test_dict.values()))
    for k in new_dict.keys():
        new_dict[k] = set()
    for i in chain(new_dict.keys()):
        for k in test_dict.keys():
            if i in test_dict[k]:
                new_dict[i].add(k)
    return new_dict


if __name__ == "__main__":
    print(remap())
