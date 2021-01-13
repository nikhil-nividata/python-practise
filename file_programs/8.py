with open("file_programs/5.txt", "r") as file_reader:
    with open("file_programs/5.copy.txt", "w") as file_writer:
        for line in file_reader:
            if not line.startswith("Generated"):
                print(line, end='')
                file_writer.write(line)
