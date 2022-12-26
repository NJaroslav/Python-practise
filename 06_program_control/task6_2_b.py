is_valid_ip = False

while not is_valid_ip:
    
    ip = input("Inter an IP address: ")
    ip_bytes = ip.split(".")
    is_valid_ip = len(ip_bytes) == 4

    for byte in ip_bytes:
        is_valid_ip  = byte.isdigit() and is_valid_ip and 0 <= int(byte) <= 255  
    if not is_valid_ip:
        print("Adress was entered incorrectly")
else:
    first_byte = int(ip.split(".")[0])

    if 1 <= first_byte <= 233:
        print("unicast")
    elif 224 <= first_byte <= 239:
        print("multicast")
    elif ip ==  "0.0.0.0":
        print("unassigned")
    elif ip == "255.255.255.255":
        print("local broadcast")
    else:
        print("unused")
