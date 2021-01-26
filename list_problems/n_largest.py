# Python Program to find N Largest numbers from the list

def get_n_largest(list_obj, n):
    list_obj.sort(reverse=True)
    return list_obj[:n]


if __name__ == "__main__":
    m = [540, 20, 102, 2312, 23, 2312, 2312, 21, 23, 12, 12, 1, 1, 344]
    n = int(input("Enter value of n : "))
    print(get_n_largest(m, n))
