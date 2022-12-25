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
