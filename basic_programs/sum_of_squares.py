def sum_of_squares(n):
    return int(n * (n + 1) * (2*n + 1) / 6)


if __name__ == "__main__":
    num = int(input("Enter a number : "))
    print("Sum of squares of first {0} NN = {1}".format(
        num,
        sum_of_squares(num)
    ))
