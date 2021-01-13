# Extract digits from tuple elements

def process():
    test_list = [(15, 3), (3, 9)]
    temp_set = set()
    for tup in test_list:
        for num in tup:
            while num > 0:
                temp_set.add(num % 10)
                num //= 10
    return temp_set


if __name__ == "__main__":
    print(process())
