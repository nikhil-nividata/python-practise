start_at = int(input("Enter start : "))
end_at = int(input("End at : "))

print(
    [x for x in filter(lambda a: a >= 0, range(start_at, end_at + 1))]
)
