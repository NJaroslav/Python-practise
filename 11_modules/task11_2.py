from task11_1 import parse_cdp_neighbors 

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

def create_network_map(filenames):
    net_map = {}
    for filename in filenames:
        with open(filename, 'r') as f:
            parsed = parse_cdp_neighbors(f.read())
            net_map.update(parsed)
    return net_map

if __name__ == "__main__":
    topology = create_network_map(infiles)
    print(topology)
    
