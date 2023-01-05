import re
from pprint import pprint

def get_ip_from_cfg(filename):
    res = {}
    r =(r'^interface (?P<intrf>\S+)'
        r'|address (?P<ip>\S+) (?P<mask>\S+)')
    with open(filename, 'r') as f:
        for line in f:
            m = re.search(r,line)
            if m:
                if m.lastgroup == 'intrf':
                    intrf = m.group('intrf')
                elif m.lastgroup == 'mask':
                    res.setdefault(intrf,[])
                    res[intrf].append(m.group('ip', 'mask'))
    return res
                
                     
if __name__ == '__main__':
    pprint(get_ip_from_cfg('config_r2.txt'))


