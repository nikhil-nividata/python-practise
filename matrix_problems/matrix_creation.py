# Creating a matrix of Dimension N
import itertools
N = 5

res = [
    list(range(1 + i * N, 1 + (i+1) * N))
    for i in range(N)
]

for r in res:
    print(r)

counter = itertools.count(1)
result = [
    [next(counter) for j in range(N)]
    for i in range(N)
]

for r in res:
    print(r)
