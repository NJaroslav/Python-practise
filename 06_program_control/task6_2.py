'''
Task #6.2

Prompt the user to enter an IP address in the format 10.0.1.1.
Depending on the type of address (described below), print to the stdout:

- ‘unicast’ - if the first byte is in the range 1-223

- ‘multicast’ - if the first byte is in the range 224-239

- ‘local broadcast’ - if the IP address is 255.255.255.255

- ‘unassigned’ - if the IP address is 0.0.0.0

- ‘unused’ - in all other cases
'''

ip = input("Inter an IP address: ")
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
    
    


