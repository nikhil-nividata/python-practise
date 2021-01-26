with open("file_programs/5.txt", "r") as file_reader:
    count = 0
    for line in file_reader:
        count += 1
    print(count)
