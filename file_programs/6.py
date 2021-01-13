find_word = "\n"

with open("file_programs/5.txt", "r") as file_reader:
    line_no = 0
    for line in file_reader:
        if line[-1] == '\n':
            line = line[:-1]
        if find_word in line.split() or find_word == '\n':
            print(line_no)
        line_no += 1
