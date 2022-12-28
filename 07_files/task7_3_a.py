table = []

with open('CAM_table.txt','r') as f:
    for line in f:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, _, interface = words
            table.append([int(vlan),mac,interface])

for vlan, mac, intf in sorted(table):
    print(f"{vlan:<9}{mac:20}{intf}")
