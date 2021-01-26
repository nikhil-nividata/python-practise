def sum_of_cubes(n):
    return int((n*(n+1)/2)**2)


if __name__ == "__main__":
    num = int(input("Enter number : "))
    print("The sum of cubes of first {0} NN is {1}".format(
        num,
        sum_of_cubes(num)
    ))
