'''

Convert the IP address in the ip variable to binary and print output in columns to stdout:

- the first line must be decimal values
- the second line is binary values

The output should be ordered in the same way as in the example output below:

- in columns
- column width 10 characters (in binary you need to add two spaces between columns to separate octets among themselves)

Example output for address 10.1.1.1:

10        1         1         1
00001010  00000001  00000001  00000001
Restriction: All tasks must be done using the topics covered in this and previous chapters.

ip = "192.168.3.1"

'''

ip = "192.168.3.1"
parts = ip.split(".")

out = """
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
"""

print(out.format(int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])))
