# Sort list of tuples by second element

def sort_it():
    inp_list = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
    return sorted(
        inp_list,
        key=lambda x: x[1]
    )


if __name__ == "__main__":
    print(sort_it())
