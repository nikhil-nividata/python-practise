
from typing import MutableSet


def position_of_nth_multiple(number, multiple_no):
    f1 = 0
    f2 = 1
    i = 2
    while True:
        f1, f2 = f2, f1+f2
        if f2 % number == 0:
            return i * multiple_no
        i += 1


if __name__ == "__main__":
    number = int(input("Enter the number whose multiple is to be found : "))
    multiple_no = int(input("Enter the multiple no : "))
    print("{0} Multiple of {1} is at Fibonacci Number {2}".format(
        multiple_no,
        number,
        position_of_nth_multiple(number, multiple_no)
    ))
