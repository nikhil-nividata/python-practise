# Factorial of a Number


def factorial(num):
    if num < 0:
        return None
    fact = 1
    while num > 1:
        fact *= num
        num -= 1
    return fact


if __name__ == "__main__":
    num = int(input("Enter a number : "))
    print("{0}! = {1}".format(num, factorial(num)))
