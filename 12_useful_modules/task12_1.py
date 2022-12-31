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
