'''
Task #15.1a

Copy the get_ip_from_cfg function from task 15.1 and redesign
it so that it returns a dictionary:

key: interface name

value: a tuple with two lines:

IP address

mask

Add to the dictionary only those interfaces on which IP addresses are configured.

Dict example (arbitrary addresses are taken):

{"FastEthernet0/1": ("10.0.1.1", "255.255.255.0"),
 "FastEthernet0/2": ("10.0.2.1", "255.255.255.0")}
To get this result, use regular expressions.

Check the operation of the function using the example of the config_r1.txt file.

Please note that in this case, you can not check the correctness of the IP address,
address ranges, and so on, since the command output from network device is processed, 
not user input.
'''

import re

def get_ip_from_cfg(filename):
    res = {}
    regex = (r'interface (?P<intrf>\S+)\n'
             r'( .*\n)*'
             r' ip address (?P<ip>\S+) (?P<mask>\S+)')
    
    with open(filename, 'r') as f:
        for m in re.finditer(regex,f.read()):
            res[m.group('intrf')] =  m.group('ip', 'mask')
    return res

if __name__ == '__main__':
    print(get_ip_from_cfg('config_r1.txt'))


