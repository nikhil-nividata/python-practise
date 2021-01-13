from datetime import *

# h1 = int(input("Enter h1 : "))
# m1 = int(input("Enter m1 : "))
# h2 = int(input("Enter h2 : "))
# m2 = int(input("Enter m2 : "))

h1 = 7
m1 = 20
h2 = 9
m2 = 45

d1 = datetime.today()
d1 = d1.replace(hour=h1).replace(minute=m1)


d2 = datetime.now()
d2 = d2.replace(hour=h2).replace(minute=m2)

delta = d2 - d1
print("{0}min {1}sec".format(
    delta.seconds // 60,
    delta.seconds % 60
))
