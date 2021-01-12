# List pairs to dictionary

def convert():
    test_dict = {
        'month': [1, 2, 3],
        'name': ['Jan', 'Feb', 'March']
    }
    return dict(zip(test_dict['month'], test_dict['name']))


if __name__ == "__main__":
    print(convert())
