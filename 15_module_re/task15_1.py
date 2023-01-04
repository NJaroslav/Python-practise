import re

def get_ip_from_cfg(filename):
    res = []
    regex = r'ip address (\S+) (\S+)'
    with open(filename, 'r') as f:
        for match in re.finditer(regex,f.read()):
            res.append(match.groups())
    return res

if __name__ == '__main__':
    print(get_ip_from_cfg('config_r1.txt'))


