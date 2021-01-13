with open("file_programs/reversed_lines.txt", "w") as file_writer:
    with open("file_programs/10.txt", "r") as file_reader:
        for line in file_reader:
            if line[-1] == '\n':
                line = line[:-1]
            file_writer.write(line[::-1] + '\n')
