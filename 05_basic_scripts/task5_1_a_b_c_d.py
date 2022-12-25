'''
Task #5.1

The task contains a dictionary with information about different devices.
In the task you need: ask the user to enter the device name (r1, r2 or sw1). 
Print information about the corresponding device to standard output (information will be in the form of a dictionary).

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}
'''

'''
Task #5.1a

Modify the script from task 5.1 so that, in addition to the device name, the script requested and then printed the device parameter as well.

Display information about the corresponding parameter of the specified device.
'''

'''
Task #5.1b

Modify the script from task 5.1a so that, when requesting a parameter, a list of possible parameters was displayed. The list of parameters must be obtained from the dictionary, rather than written manually.

Display information about the corresponding parameter of the specified device.
'''

'''
Task #5.1c

Copy and modify the script from task 5.1b so that when you request a parameter that is not in the device dictionary, the message ‘There is no such parameter’ is displayed. The assignment applies only to the parameters of the devices, not to the devices themselves.

Note

Try typing a non-existent parameter, to see what the result will be. And then complete the task.

If an existing parameter is selected, print information about the corresponding parameter.
'''

'''
Task #5.1d

Modify the script from task 5.1c so that, when requesting a parameter, the user could enter the parameter name in any case.
'''

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}

device = input("Input the name of device:\n")
param = input("Input the parametrs ({}) : \n".format(",".join(london_co[device].keys()))).lower()

print(london_co[device].get(param,"There is no such a parameter"))
