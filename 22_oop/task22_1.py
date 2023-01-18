class Topology:
    def __init__(self, topology_dict):
        self.topology = {}
        for f,s in topology_dict.items():
            if not self.topology.get(s) == f:
                self.topology[f] = s

if __name__ == "__main__":
    topology_dict = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0")
    }
    t = Topology(topology_dict)
    print(t.topology)
                        

