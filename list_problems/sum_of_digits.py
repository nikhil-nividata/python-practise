# Sum Of Digits

m = [12, 45, 23, 66, 12]

n = []

for num in m:
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    n.append(sum)

print(n)
