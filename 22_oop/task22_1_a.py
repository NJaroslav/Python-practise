class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)
        
    def _normalize(self, topology_dict):
        tmp = {}
        for f,s in topology_dict.items():
            if not tmp.get(s) == f:
                tmp[f] = s
        return tmp

if __name__ == "__main__":
    topology_dict = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0")
    }
    t = Topology(topology_dict)
    print(t.topology)
                        

