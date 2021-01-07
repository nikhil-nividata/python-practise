# A Python Program to remove empty list from a list

m = [1, 2, 3, 4, [], [], [], (), ()]

m = [x for x in m if x != [] and x != ()]

print(m)
