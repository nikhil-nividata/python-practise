with open("file_programs/reverse_with_stack.txt", "w") as file_writer:
    with open("file_programs/10.txt", "r") as file_reader:
        stack = []
        for line in file_reader:
            if line[-1] == '\n':
                line = line[:-1]
            stack.append(line)
        while len(stack) > 0:
            file_writer.write(stack.pop() + '\n')
