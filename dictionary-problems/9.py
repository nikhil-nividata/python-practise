# Using Ordered dictionary check for a pattern

def check():
    from typing import OrderedDict
    string = "engirocks"
    pattern = "ngo"
    ptrlen = 0
    for key in OrderedDict.fromkeys(string).keys():
        if (key == pattern[ptrlen]):
            ptrlen += 1
            if ptrlen == len(pattern):
                return True
    return False


if __name__ == "__main__":
    print(check())
