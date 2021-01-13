import time
import datetime


def method1():
    string = "20/01/2020"
    print(datetime.datetime.strptime(string, "%d/%m/%Y").timestamp())


if __name__ == "__main__":
    method1()
