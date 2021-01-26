# Check if a number is Fibonacci Number
from math import sqrt


def is_perfect_square(num):
    return int(sqrt(num)) ** 2 == num


def is_fibonacci(num):
    if (
        is_perfect_square(5 * num**2 - 4)
        or
        is_perfect_square(5 * num**2 + 4)
    ):
        return True
    return False


if __name__ == "__main__":
    x = int(input("Enter a number : "))
    print("{0} is {1} number".format(
        x,
        "Fibonacci" if is_fibonacci(x) else "not Fibonacci"
    ))
