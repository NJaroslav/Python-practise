from sys import argv

file_in_name = argv[1]
file_out_name = argv[2]

ignore = ["duplex", "alias", "configuration"]

with open(file_in_name,'r') as src,  open(file_out_name,'w') as out:
    for line in src:
        is_ignored = set(line.split()) & set(ignore)
        if not is_ignored and not line.startswith('!'):
            out.write(line)
