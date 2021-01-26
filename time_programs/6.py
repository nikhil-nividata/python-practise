import time

print("Press ENTER to count laps.\nPress CTRL+C to stop")

start_time = time.time()
last_time = start_time
lap_number = 1

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print("Lap no : {0}".format(lap_number))
        print("Lap Time : {0}".format(lap_time))
        print("Total Time : {0}".format(total_time))
        lap_number += 1
        last_time = time.time()
        print()
        print("*"*20)
        print()
except KeyboardInterrupt:
    print("Done")
