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
        
