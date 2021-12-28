

class Node:

    def __init__(self, Id: int, pos: tuple):
        self.id = Id
        self.pos = pos
        self.weight = float('inf')
        self.Tag = -1
        self.prev = None

    def __str__(self):
        return str(self.id)

    def get_id(self):
        return self.id

    def get_tag(self):
        return self.Tag

    def set_tag(self, t):
        self.Tag = t

    def set_prev(self, p):
        self.prev = p

    def get_prev(self):
        return self.prev

    def get_weight(self):
        return self.weight

    def set_weight(self, w):
        self.weight = w

    def get_pos(self):
        return self.pos

    def pos_to_string(self):
        string = "{},{},{}".format(self.pos[0], self.pos[1], self.pos[2])
        return string


class Edge:
    def __init__(self, src: int, dest: int, weight: float):
        self.src = src
        self.dest = dest
        self.weight = weight
        self.Tag = 0
        self.info = " "

    def getSrc(self):
        return self.src

    def getDest(self):
        return self.dest

    def getWeight(self):
        return self.weight


from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    NodeDict = {}
    dictFather = {}   # to src->dest
    dictOfChild = {}  # dest->src
    edge_size = 0
    Mc = 0

    def __init__(self):
        self.NodeDict = {}
        self.dictFather = {}
        self.dictOfChild = {}
        self.edge_size = 0
        self.Mc = 0

    def get_nodeList(self):
        return self.NodeDict

    def get_node(self, id):
        return self.NodeDict.get(id)

    def get_dictFather(self):
        return self.dictFather

    def v_size(self) -> int:
        return len(self.Nodedict)

    def e_size(self) -> int:
        var = self.edge_size
        return var

    def get_all_v(self) -> dict:
        return self.dictFather

    # return a dictionary of all the nodes connected to (into) node_id ,each node is represented using a pair
    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.dictOfChild[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.dictFather[id1]

    def get_mc(self) -> int:
        return self.Mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        print(str(self.NodeDict))
        if id1 in self.NodeDict.keys() and id2 in self.NodeDict.keys():  # check if the node id exists
            if self.NodeDict.get(id1) is not None and self.NodeDict.get(id2) is not None:
                edge = Edge(id1, id2, weight)   # new edge
                self.dictFather[id1][id2] = edge
                self.dictOfChild[id2][id1] = edge
                self.Mc = self.Mc + 1
                self.edge_size += 1

            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.NodeDict.keys():  # we check if the node id already exists
            n = Node(node_id, pos)  # new node
            self.NodeDict[node_id] = n
            self.dictFather[node_id] = {}
            self.dictOfChild[node_id] = {}
            self.Mc += 1

            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.NodeDict:
            for e in list(self.dictOfChild[node_id]):
                self.remove_edge(e, node_id)  # remove from the edges
                self.remove_edge(node_id, e)  # remove from the edges
            del self.NodeDict[node_id]       # remove the node
            self.Mc += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id2 in self.dictFather[node_id1]:
            del self.dictFather[node_id1][node_id2]      # remove from src to dest
            if node_id1 in self.dictOfChild[node_id2]:
                del self.dictOfChild[node_id2][node_id1]    # remove from dest to src
                self.edge_size -= self.edge_size
                self.Mc += 1
                return True
        self.Mc += 1
        return False


