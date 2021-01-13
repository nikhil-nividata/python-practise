with open("file_programs/9.txt", "r") as file_reader:
    with open("file_programs/9.copy.txt", "w") as file_writer:
        seen = set()
        for line in file_reader:
            if line[-1] == '\n':
                line = line[:-1]
            if line not in seen:
                print(line)
                seen.add(line)
                file_writer.write(line + '\n')
