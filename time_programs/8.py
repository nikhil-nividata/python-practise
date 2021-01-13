# Convert timestamp to Date Time Object
from datetime import datetime, time


def method1():
    timestamp = 1545730073
    print(datetime.fromtimestamp(timestamp))


if __name__ == "__main__":
    method1()
