m = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
i = 0
n = []
index = 0
for num in m:
    if num in m[index + 1:]:
        if num not in n:
            n.append(num)
    index += 1

print(n)
