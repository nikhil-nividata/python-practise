# Sort Dicrionary

def sort_it():
    test_dict = {
        2: '64',
        1: '69',
        4: '23',
        5: '65',
        6: '34',
        3: '76'
    }
    return sorted(
        [(k, v) for k, v in test_dict.items()],
        key=lambda i: i[0]
    )


if __name__ == "__main__":
    print(sort_it())
