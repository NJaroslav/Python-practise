with open('CAM_table.txt','r') as f:
    for line in f:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, _, interface = words
            print(f"{vlan:10}{mac:25}{interface:5}")
