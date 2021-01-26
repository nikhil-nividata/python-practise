with open("file_programs/1.txt", "r") as file_reader:
    for line in file_reader:
        for word in line.split():
            print(word)
