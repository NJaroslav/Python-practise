def convert_ranges_to_ip_list(ip_ranges):
    ips = []
    for ip in ip_ranges:
        if '-' not in ip:
            ips.append(ip)
        else:
            ip_range = ip.split('-')
            ip1_last_oct = ip_range[0].split('.')[-1]
            ip2_last_oct = ip_range[1].split('.')[-1]
            
            count = int(ip2_last_oct) - int(ip1_last_oct) + 1
            
            for c in range(count):
                ips.append(ip_range[0].replace(
                                       ip1_last_oct,
                                       str(int(ip1_last_oct) + c)
                                       ))
    return ips

if __name__ == '__main__':
    print(convert_ranges_to_ip_list(['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']))

                
                                            
                
            
            
            
