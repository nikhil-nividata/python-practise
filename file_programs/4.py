counts = {}

with open('file_programs/4.txt', "r") as file_reader:
    for line in file_reader:
        if line[-1] == '\n':
            line = line[:-1]
        counts[line] = counts.get(line, 0) + 1

print(counts)
