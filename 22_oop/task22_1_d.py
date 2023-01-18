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
            print("There is no such a link")
    
    def delete_node(self, node):
        present = 0
        for f,s in list(self.topology.items()):
            if node in f or node in s:
                del self.topology[f]
                present = 1
        if not present:
            print("There is no such a node")
    
    def add_link(self, src, dest):
        if self.topology.get(src) == dest or self.topology.get(dest) == src:
            print("Such a connection already exists")
        elif src in self.topology.keys() or src in self.topology.values() or\
            dest in self.topology.keys() or dest in self.topology.values():
            print("A link to one of the ports exists")
        else:
            self.topology[src] = dest
        

if __name__ == "__main__":
    topology_dict = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0")
    }
    t = Topology(topology_dict)
    t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
    t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
    print(t.topology)
                        

