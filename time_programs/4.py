from time import time


time_str = "08:05:45 PM"

if (time_str[-2:] == "PM"):
    x = int(time_str[:2]) + 12
    time_str = str(x) + time_str[2:]

time_str = time_str[:-2]

print(time_str)
