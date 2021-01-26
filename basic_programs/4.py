# Calculating Simple Interest

principle = float(input("Enter the principle amount : "))
interest = float(input("Enter the interest : "))
time = int(input("Enter the time period : "))


def calculate_interest(principle, interest, time):
    return principle * time * interest / 100


print(
    "Intrest {0}".format(calculate_interest(principle, interest, time))
)
