'''

Convert MAC address in mac string to binary string like this: 101010101010101010111011101110111100110011001100

Print the resulting new string to the standard output (stdout) using print.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

mac = "AAAA:BBBB:CCCC"

'''

mac = "AAAA:BBBB:CCCC"
bin_mac = "{:b}".format(int(mac.replace(":", ""), 16))
print(bin_mac)
