# Primes in an interval


def get_prime_nos(limit):
    '''
        Earthothen's Sieve

        A function that calculates the prime numbers upto a given number using Earthothen's sieve
    '''
    sieve = [x for x in range(2, limit + 1)]
    for x in sieve:
        if x == -1:
            continue
        index = 2*x - 2
        while index < len(sieve):
            sieve[index] = -1
            index += x
    return [x for x in sieve if x != -1]


if __name__ == "__main__":
    start_num = int(input("Enter the starting number : "))
    end_num = int(input("Enter the last number : "))
    primes = get_prime_nos(end_num)
    for prime in primes:
        if (prime >= start_num):
            print(prime, end=' ')
    print()
