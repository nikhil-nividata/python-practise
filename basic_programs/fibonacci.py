# Calculating the Fibonacci number

def fibonacci(num):
    fibs = [0, 1]
    n = num - 2
    while n > 0:
        fibs.append(fibs[-1] + fibs[-2])
        n -= 1
    return fibs


if __name__ == "__main__":
    n = int(input("Enter the value of n : "))
    print("Fibbonaci number {0} is {1}".format(
        n,
        fibonacci(n)[-1]
    ))
