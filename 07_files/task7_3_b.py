vlans = input("Input vlan number: ")

table = []

with open('CAM_table.txt','r') as f:
    for line in f:
        words = line.split()
        if words and words[0].isdigit() and words[0] == vlans:
            vlan, mac, _, interface = words
            print(f"{vlan:<9}{mac:20}{interface}")
            
