'''
Task #7.2

Create a script that will process the config_sw1.txt configuration file. 
The filename is passed as an argument to the script.

The script should return to the stdout commands from the passed configuration file,
excluding lines that start with ‘!’.

There should be no blank lines in the output.
'''

from sys import argv

file_name = argv[1]

with open(file_name,'r') as f:
    for line in f:
        if(line.startswith('!')):
            continue
        print(line.rstrip())
