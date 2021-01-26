# Calcuating the Compound Interest

principle = float(input("Enter the principle amount : "))
interest = float(input("Enter the interest : "))
time = int(input("Enter the time period : "))


def calculate_interest(principle, interest, time):
    return ((1 + interest / 100)**time - 1) * principle


print("Compound Intrest is {0}".format(calculate_interest(
    principle,
    interest,
    time
)))
