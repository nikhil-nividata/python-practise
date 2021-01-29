from threading import Thread, Lock, current_thread
from time import sleep
from queue import Queue


def worker(q, lock):
    while True:
        value = q.get()

        with lock:
            print(f"Thread : {current_thread().name} Value {value}")

        q.task_done()


q = Queue()
lock = Lock()
num_threads = 10

for i in range(num_threads):
    thread = Thread(target=worker, daemon=True, args=(q, lock))
    thread.start()

for i in range(21):
    q.put(i)

q.join()

print("All Tasks Completed")
