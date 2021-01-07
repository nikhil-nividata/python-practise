# Check if a number is Prime or Not

def is_prime(num):
    if (num <= 1):
        return False
    if (num <= 3):
        return True
    for n in (2, num//2):
        if num % n == 0:
            return False
    return True


num = int(input("Enter a number : "))

print("{0} is {1}".format(
    num,
    "prime" if is_prime(num) else "not prime"
))
