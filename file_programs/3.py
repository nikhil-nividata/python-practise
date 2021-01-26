counts = {
    "chars": 0,
    "spaces": 0,
    "words": 0,
    "lines": 0,
    "tabs": 0
}

with open("file_programs/1.txt", "r") as file_reader:
    for line in file_reader:
        counts["chars"] += len(line)
        counts["lines"] += 1
        counts["tabs"] += line.count('\t')
        counts["spaces"] += line.count(' ')
        counts["words"] += len(line.split())

print(counts)
