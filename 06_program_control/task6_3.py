'''
Task #6.3
A configuration generator for access ports is made in the script.
Make a similar configuration generator for trunk ports.

In trunks, the situation is complicated by the fact that there can be many VLANs, 
and you need to understand what to do with them (add, delete, overwrite).

Therefore, in accordance with each port there is a list and the first (zero index)
element of the list specifies how to interpret VLAN numbers that follow.

Dict value and corresponding command:

['add', '10', '20'] - switchport trunk allowed vlan add 10,20
['del', '17'] - switchport trunk allowed vlan remove 17
['only', '11', '30'] - switchport trunk allowed vlan 11,30

Task for ports 0/1, 0/2, 0/4:

generate a configuration based on the trunk_template template
taking into account the keywords add, del, only
The code should not be tied to specific port numbers. I.e, if there are other interface numbers in the trunk dictionary, the code should work.

access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

for intf, vlan in access.items():
    print("interface FastEthernet" + intf)
    for command in access_template:
        if command.endswith("access vlan"):
            print(f" {command} {vlan}")
        else:
            print(f" {command}")
'''

access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

for intf, vlan in trunk.items():
    print("interface FastEthernet" + intf)
    action = (
        vlan[0].replace("only", "")
               .replace("del", " remove")
               .replace("add", " add")
    )
    vlans = ",".join(vlan[1:])   
    for command in access_template:
        if command.endswith("access vlan"):
            print(f" {command} {action} {vlans}")
        else:
            print(f" {command}")

