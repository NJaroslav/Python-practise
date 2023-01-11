import csv
import re

def write_dhcp_snooping_to_csv(filenames, output):
    r = r"(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)"
    with open(output, 'w') as out:
        writer = csv.writer(out)
        writer.writerow(["switch", "mac", "ip", "vlan", "interface"])
        for fname in filenames:
            sw = fname.split('_')[0]
            with open(fname, 'r') as f:
                for line in f:
                    match = re.search(r,line)
                    if match:
                        writer.writerow((sw,) + match.groups())

if __name__ == '__main__':
    write_dhcp_snooping_to_csv(["sw1_dhcp_snooping.txt"], "out.csv")

