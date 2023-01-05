'''
Task #15.2

Create a convert_to_dict function that expects two arguments:

* a list with field names
* list of tuples with values

The function returns the result in the form of a list of dictionaries,
where the keys are taken from the first list, and the values are 
substituted from the second.

For example, if the functions are passed as arguments a list of headers and a list of
[('R1', '12.4(24)T1', 'Cisco 3825'),
 ('R2', '15.2(2)T1', 'Cisco 2911')]
 
The function should return the following list with dictionaries:

[{'hostname': 'R1', 'ios': '12.4(24)T1', 'platform': 'Cisco 3825'},
{'hostname': 'R2', 'ios': '15.2(2)T1', 'platform': 'Cisco 2911'}]

The function should not be tied to specific data or the number
of headers/data in tuples.

Check the function operation:
* the first argument is a list of headers
* the second argument is the data list

Restriction: All tasks must be performed using only the topics covered.
'''


import re

headers = ["hostname", "ios", "platform"]

data = [
    ("R1", "12.4(24)T1", "Cisco 3825"),
    ("R2", "15.2(2)T1", "Cisco 2911"),
    ("SW1", "12.2(55)SE9", "Cisco WS-C2960-8TC-L"),
]

def convert_to_dict(headers, sh_list):
    return [dict(zip(headers,sh)) for sh in sh_list]

if __name__ == '__main__':
    print(convert_to_dict(headers,data))
