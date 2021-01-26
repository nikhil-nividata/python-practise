with open("file_programs/10.txt", "r") as file_reader:
    with open("file_programs/odd.txt", "w") as file_writer:
        line_no = 0
        for line in file_reader:
            if line_no % 2 == 0:
                file_writer.write(line)
            line_no += 1
