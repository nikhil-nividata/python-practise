with open("file_programs/merged.txt", "w") as file_writer:
    with open("file_programs/10.txt", "r") as file_reader1:
        for line in file_reader1:
            file_writer.write(line)
    file_writer.write('\n')
    with open("file_programs/odd.txt", "r") as file_reader2:
        for line in file_reader2:
            file_writer.write(line)
