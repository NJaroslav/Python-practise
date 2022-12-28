'''
Task #7.2(b)

Make a copy of the code from the task 7.2a. Add this functionality:
instead of printing to stdout, 
the script should write the resulting lines to a file.

File names must be passed as arguments to the script:

- name of the source configuration file
- name of the destination configuration file

In this case, the lines that are contained in the ignore list and lines that start with ! must be filtered.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

ignore = ["duplex", "alias", "Current configuration"]
'''

from sys import argv

file_in_name = argv[1]
file_out_name = argv[2]

ignore = ["duplex", "alias", "configuration"]

with open(file_in_name,'r') as src,  open(file_out_name,'w') as out:
    for line in src:
        is_ignored = set(line.split()) & set(ignore)
        if not is_ignored and not line.startswith('!'):
            out.write(line)
