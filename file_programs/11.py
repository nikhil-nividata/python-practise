with open("file_programs/9.copy.txt", "r") as file_reader:
    with open("file_programs/9.txt", "a") as file_appender:
        for line in file_reader:
            file_appender.write(line)
