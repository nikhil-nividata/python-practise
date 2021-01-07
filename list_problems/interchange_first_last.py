# Python program to interchange the first and last elements of a list

def exchange(list_obj):
    list_obj[0], list_obj[-1] = list_obj[-1], list_obj[0]
    return list_obj


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(exchange(nums))
