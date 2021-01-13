# Remove the elements of length K
def rem():
    test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
    K = 2
    return [
        x
        for x in test_list
        if len(x) != K
    ]


def using_lambda():
    test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
    K = 2
    return list(filter(
        lambda elem: len(elem) != K,
        test_list
    ))


if __name__ == "__main__":
    print(rem())
    print(using_lambda())
