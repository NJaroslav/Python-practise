'''

Convert string in mac variable from XXXX:XXXX:XXXX format to XXXX.XXXX.XXXX format.

Print the resulting new string to the standard output (stdout) using print.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

mac = "AAAA:BBBB:CCCC"

'''

mac = "AAAA:BBBB:CCCC"
mac_replaced = mac.replace(":", ".")
print(mac_replaced)
