# Check for Armstrong Number


def check_armstrong(num):
    power = len(num)
    newNum = 0
    for i in num:
        newNum += int(i)**power
    return newNum == int(num)


if __name__ == "__main__":
    num = input("Enter number : ")
    print("{0} is {1}Armstrong Number".format(
        num,
        "" if check_armstrong(num) else "not "
    ))
