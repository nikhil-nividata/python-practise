# Program to calculate the Cumulative Sum of a list

m = [1, 2, 3, 4, 5, 6]
n = [m[0]]

index = 1

while index < len(m):
    n.append(n[-1] + m[index])
    index += 1

print(n)
