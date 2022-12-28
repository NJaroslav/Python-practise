'''
Task #7.2(a)

Make a copy of the code from the task 7.2.

Add this functionality: The script should not print to the stdout commands, which contain words from the ignore list. 
The script should also not print lines that begin with !.

Check the script on the config_sw1.txt configuration file. The filename is passed as an argument to the script.

ignore = ["duplex", "alias", "Current configuration"]
'''


from sys import argv

file_name = argv[1]

ignore = ["duplex", "alias", "configuration"]

with open(file_name,'r') as f:
    for line in f:
        is_ignored = set(line.split()) & set(ignore)
        if not is_ignored and not line.startswith('!'):
            print(line.rstrip())
