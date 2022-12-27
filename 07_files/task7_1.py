'''
Task #7.1

Process the lines from the ospf.txt file and print information for each line in this form to the stdout:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Restriction: All tasks must be done using the topics covered in this and previous chapters.
'''
out_template = '''
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
'''

with open('ospf.txt', 'r') as f:
    for line in f:
        line = line.replace(',','').replace('[','').replace(']','')
        line = line.split()
        print(out_template.format(
            line[1],
            line[2],
            line[4],
            line[5],
            line[6]
        ))
    
