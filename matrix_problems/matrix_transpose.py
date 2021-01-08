# Python Code to transpose Matrix
m = [
    [1, 2],
    [3, 4],
    [5, 6]
]

m_transpose = map(list, zip(*m))

for x in m_transpose:
    print(x)
