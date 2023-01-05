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


