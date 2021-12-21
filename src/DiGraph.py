class Node:

    def __init__(self, Id: int, pos: tuple):
        self.id = Id
        self.pos = pos
        self.weight = 0
        self.info = None
        self.Tag = 0


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

    def v_size(self) -> int:
        return len(self.Nodedict)

    def e_size(self) -> int:
        var = self.edge_size
        return var

    def get_all_v(self) -> dict:
        return self.dictFather

    # return a dictionary of all the nodes connected to (into) node_id ,each node is represented using a pair
    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.dictOfChild

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.dictFather

    def get_mc(self) -> int:
        return self.Mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 and id2 in self.NodeDict.keys():  # check if the node id exists
            if self.NodeDict[id1] is not None and self.NodeDict[id2] is not None and id1 != id2:
                self.dictFather[id2].update({id1, weight})
                self.dictOfChild[id1].update({id2, weight})
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.NodeDict.keys():  # we check if the node id already exists
            n = Node(node_id, pos)  # new node
            self.NodeDict[node_id] = n
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        for e in list(self.dictOfChild[node_id]):
            self.remove_edge(e, node_id)  # remove from the edges
            self.remove_edge(node_id, e)  # remove from the edges

        del self.NodeDisct[node_id]  # remove the node
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id2 in self.dictFather.keys() and node_id2 in self.dictOfChild.keys():
            del self.dictFather[node_id2][node_id1]  # remove from src to dest
            del self.dictOfChild[node_id1][node_id2]  # remove from dest to src
            return False
        return False
