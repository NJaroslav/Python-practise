'''
Task #5.3

The script should prompt the user for input:

- interface mode (access/trunk)
- interface number (Gi0/3)
- VLAN number (for trunk mode, a list of VLANs will be entered)

Depending on the selected mode,print corresponding access or trunk
configuration on stdout.

The output should first print the interface line and the interface number, 
and then the corresponding template in which the VLAN number
(or the list of VLANs) is inserted.
'''

'''
Task #5.3(a)
Copy and change the script from task 5.3 in such a way that,
depending on the selected mode, different questions were asked 
in the request for the VLAN number or VLAN list:

- for access: ‘Enter VLAN number:’
- for trunk: ‘Enter the allowed VLANs:’

access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]
'''


access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

vlan_mode_depending = {
    "trunk"  : "Enter the allowed VLANs: ",
    "access" : "Enter VLAN number:"
}

interface_mode = input("Enter interface mode (access/trunk): ")
interface_number = input("Enter type and interface number: ")

vlan_number = input(vlan_mode_depending[interface_mode])
type_template = {"access" : access_template, "trunk" : trunk_template}


print("interface" + interface_number)

print("\n".join(type_template[interface_mode]).format(vlan_number))
