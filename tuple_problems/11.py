# Ordering Tuple List wrt another List

def sort_it():
    test_list = [('Gfg', 10), ('best', 3), ('CS', 8), ('Geeks', 7)]
    ord_list = ['Geeks', 'best', 'CS', 'Gfg']
    temp_dict = {
        k: val
        for k, val in test_list
    }
    return [
        (k, temp_dict[k])
        for k in ord_list
    ]


if __name__ == "__main__":
    print(sort_it())
