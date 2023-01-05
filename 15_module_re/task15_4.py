import re

def get_ints_without_description(filename):
    r = re.compile(r'interface (?P<intf>\S+)\n'
                   r'(?P<desc> description \S+)?')
    with open(filename, 'r') as f:
        match = r.finditer(f.read())
        return [m.group('intf') for m in match if m.lastgroup == 'intf']


if __name__ == '__main__':
    print(get_ints_without_description('config_r1.txt'))
