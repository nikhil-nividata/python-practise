# Tuple of cube

def tuple_of_cubes():
    inp_list = [1, 2, 3]
    return [(x, x**3) for x in inp_list]


if __name__ == "__main__":
    print(tuple_of_cubes())
