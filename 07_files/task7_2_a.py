from sys import argv

file_name = argv[1]

ignore = ["duplex", "alias", "configuration"]

with open(file_name,'r') as f:
    for line in f:
        is_ignored = set(line.split()) & set(ignore)
        if not is_ignored and not line.startswith('!'):
            print(line.rstrip())
