'''
Task 5.2

Ask the user to enter the IP network in the format: 10.1.1.0/24.

Then print information about the network and mask in this format:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
'''

socket = input("Input Ip network:\n")

ip_template = """ 
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
"""

mask_template = """
Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
"""

bin_ip_template = """
{:08b}{:08b}{:08b}{:08b}
"""

ip,mask = socket.split("/")

gr1,gr2,gr3,gr4 = ip.split(".")

binary_mask = "1" * int(mask) + "0" * (32 - int(mask))

m1,m2,m3,m4 = [
    int(binary_mask[0:8], 2),
    int(binary_mask[8:16], 2),
    int(binary_mask[16:24], 2),
    int(binary_mask[24:32], 2)
]

bin_ip = bin_ip_template.format(int(gr1),int(gr2),int(gr3),int(gr4))
bin_s = bin_ip[:int(mask)] + "0" * (32 - int(mask))

n1,n2,n3,n4 = [
    int(bin_s[0:8], 2),
    int(bin_s[8:16], 2),
    int(bin_s[16:24], 2),
    int(bin_s[24:32], 2)
]



print(ip_template.format(n1,n2,n3,n4))
print(mask_template.format(int(mask),m1,m2,m3,m4))


