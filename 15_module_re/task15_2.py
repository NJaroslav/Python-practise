'''
Task 15.2
Create a function parse_sh_ip_int_br that expects as an argument the name of the
file containing the output of the show ip int br command.

The function should process the output of the show ip int br command and return
the following fields:

Interface

IP-Address

Status

Protocol

The information should be returned as a list of tuples:

[("FastEthernet0/0", "10.0.1.1", "up", "up"),
 ("FastEthernet0/1", "10.0.2.1", "up", "up"),
 ("FastEthernet0/2", "unassigned", "down", "down")]
To get this result, use regular expressions.

Check the operation of the function using the example of the sh_ip_int_br.txt file.
'''


import re
from pprint import pprint

def parse_sh_ip_int_br(filename):
    res = []  
    r = (r'(\S+) +(\S+) +\w+ +\w+ +(\S+) +(up|down)')
    with open(filename, 'r') as f:
        res = [m.groups() for m in re.finditer(r,f.read())]
    return res


if __name__ == '__main__':
    pprint(parse_sh_ip_int_br('sh_ip_int_br.txt'))
        
