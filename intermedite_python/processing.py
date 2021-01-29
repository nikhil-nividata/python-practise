from multiprocessing import Process, Queue, Value, Array, Lock
from time import sleep
import os


def square(nums, q):
    for num in nums:
        q.put(num**2)


def negate(nums, q):
    for num in nums:
        q.put(-num)


nums = range(1, 6)
q = Queue()

p1 = Process(target=square, args=(nums, q))
p2 = Process(target=negate, args=(nums, q))

p1.start()
p2.start()

p1.join()
p2.join()

while not q.empty():
    print(q.get())
