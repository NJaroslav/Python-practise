'''
Task #6.2a

Make a copy of the code from the task 6.2.

Add verification of the entered IP address. An IP address is considered correct if it:

- consists of 4 numbers (not letters or other symbols)
- numbers are separated by a dot
- every number in the range from 0 to 255

If the IP address is incorrect, print the message: ‘Invalid IP address’
The message “Invalid IP address” should be printed only once, even if several points above are not met.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
'''


ip = input("Inter an IP address: ")
ip_bytes = ip.split(".")
is_valid_ip = len(ip_bytes) == 4

for byte in ip_bytes:
    is_valid_ip  = byte.isdigit() and is_valid_ip and 0 <= int(byte) <= 255  

if is_valid_ip:

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
else:
    print("Invalid IP address")


