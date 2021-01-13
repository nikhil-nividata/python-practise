with open("file_programs/1.txt", "r") as file_reader:
    while True:
        char = file_reader.read(1)
        if not char:
            break
        print(char)
