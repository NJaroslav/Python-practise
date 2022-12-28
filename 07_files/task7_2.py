from sys import argv

file_name = argv[1]

with open(file_name,'r') as f:
    for line in f:
        if(line.startswith('!')):
            continue
        print(line.rstrip())
