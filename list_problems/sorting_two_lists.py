# A Python Program to sort One list using another list

def get_val(e):
    return e[1]


# list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list1 = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
list2 = [0,   1,   1,    0,   1,   2,   2,   0,   1]


im = [x for x in zip(list1, list2)]

print(im)

im.sort(key=get_val)

sorted = [x for x, y in im]

print(sorted)
