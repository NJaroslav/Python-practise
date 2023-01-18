class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)
        
    def _normalize(self, topology_dict):
        tmp = {}
        for f,s in topology_dict.items():
            if not tmp.get(s) in f:
                tmp[f] = s
        return tmp
    
    def delete_link(self, from_port, to_port):
        if self.topology.get(from_port) == to_port:
            del self.topology[from_port]
        elif self.topology.get(to_port) == from_port:
            del self.topology[to_port]
        else:
            print("There is no such link")

if __name__ == "__main__":
    topology_dict = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0")
    }
    t = Topology(topology_dict)
    t.delete_link(('R555551', 'Eth0/0'), ('SW1', 'Eth0/1'))
                        

