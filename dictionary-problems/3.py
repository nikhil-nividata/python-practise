# Sorting a list of Dictionaries

def lambda_sort():
    lis = [
        {"name": "Nandini", "age": 20},
        {"name": "Manjeet", "age": 20},
        {"name": "Nikhil", "age": 22},
        {"name": "Nikhil", "age": 19}
    ]

    return sorted(lis, key=lambda i: (i['age'], i['name']))


def itemgetter_sort():
    lis = [
        {"name": "Nandini", "age": 20},
        {"name": "Manjeet", "age": 20},
        {"name": "Nikhil", "age": 22},
        {"name": "Nikhil", "age": 19}
    ]
    from operator import itemgetter
    return sorted(
        lis,
        key=itemgetter('age', 'name')
    )


if __name__ == "__main__":
    print(lambda_sort())
    print(itemgetter_sort())
