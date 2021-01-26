# Number of times a day comes in a year
import datetime
import calendar

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

day_count = {
    key: 52
    for key in days
}

year = input("Enter the year : ")

dayIndex = datetime.datetime.strptime("01 01 " + year, "%d %m %Y").weekday()

day = calendar.day_name[dayIndex]

day_count[day] += 1

if int(year) % 4 == 0:
    if int(year) % 100 == 0:
        if int(year) % 400 == 0:
            day = calendar.day_name[dayIndex + 1]
            day_count[day] += 1
    else:
        day = calendar.day_name[dayIndex + 1]
        day_count[day] += 1

print(day_count)
