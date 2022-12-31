'''
Task 12.1

Create a ping_ip_addresses function that checks if IP addresses are pingable.

The function expects a list of IP addresses as an argument.

The function must return a tuple with two lists:

list of available IP addresses

list of unavailable IP addresses

To check the availability of an IP address, use the ping command.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

'''

import subprocess

def ping_ip_adresses(ip_adresses):
    reachable = []
    unreachable = []
    
    for ip in ip_adresses:
        res = subprocess.run(['ping', '-c', '2', ip],
                             stdout = subprocess.DEVNULL,
                             stderr = subprocess.DEVNULL
                            )
        if res.returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)
    return (reachable,unreachable)

if __name__ == "__main__":
    print(ping_ip_adresses(['8.8.8.8']))
