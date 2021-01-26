# A Python Program to chunk up a a list

m = [x for x in range(20)]

n = int(input("Enter slice size : "))
x = []
rem = len(m)
index = 0
while rem > 0:
    x.append(m[index: index + n])
    index += n
    rem -= n

print(x)
