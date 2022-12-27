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
    
