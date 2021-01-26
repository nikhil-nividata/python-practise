n = 3
with open("file_programs/5.txt", "r") as file_reader:
    for line in file_reader:
        for word in line.split():
            if len(word) == n:
                print(word)
