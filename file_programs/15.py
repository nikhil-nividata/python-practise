with open("file_programs/merged.txt", "r") as file_reader:
    lines = file_reader.readlines()
    with open("file_programs/reverse.txt", "w") as file_writer:
        for line in reversed(lines):
            if line[-1] != '\n':
                line += '\n'
            file_writer.write(line)
