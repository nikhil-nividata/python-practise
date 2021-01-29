from functools import wraps


def doSomethingBeforeHi(x):
    def midman(func_ref):
        @wraps(func_ref)
        def wrapper():
            print(f"Will execute functuion {x}")
            func_ref()
            print("Executed Function")
        return wrapper
    return midman


@doSomethingBeforeHi("LOL")
def hi(name='Nikhil'):
    print(f"Hello There {name}")


hi()


class doSomethingWithClass(object):

    def __init__(self, x):
        self.x = x

    def __call__(self, fxn=None):
        if fxn == None:
            return self._wrap()
        else:
            self.fxn = fxn
            return self

    def _wrap(self):
        print(f"Will execute the function {self.x}")
        self.fxn()
        print("Executed the Fxn")


@doSomethingWithClass("LOL")
def hello(name="Nikhil"):
    print(f"Hello there {name}")


print(hello)
print(hello.__dict__)
print(hello())
