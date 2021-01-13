dict_from_file = {}
with open("file_programs/10.txt", "r") as file_reader:
    for line in file_reader:
        if line == '':
            continue
        if line[-1] == '\n':
            line = line[1:-1]
        line = line.strip('{}')
        for kv in line.split(', '):
            kv_tuple = kv.split(': ')
            dict_from_file[
                kv_tuple[0].strip('\'\"')
            ] = kv_tuple[1].strip('\'\"')

print(dict_from_file)
