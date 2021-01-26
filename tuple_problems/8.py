def combinations():
    test_tuple1 = (9, 2)
    test_tuple2 = (7, 8)
    res = []
    for x in test_tuple1:
        for y in test_tuple2:
            res.append((x, y))
            res.append((y, x))
    return res


def using_itertools():
    test_tuple1 = (9, 2)
    test_tuple2 = (7, 8)
    from itertools import chain, product
    return list(
        chain(
            product(
                test_tuple1,
                test_tuple2
            ),
            product(
                test_tuple2,
                test_tuple1
            )
        )
    )


if __name__ == "__main__":
    print(combinations())
    print(using_itertools())
