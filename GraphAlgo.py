import json
import math
import random
import matplotlib.pyplot as plt

from turtledemo.chaos import g, plot
from typing import List, Type, Any

from src import GraphInterface
from src.DiGraph import DiGraph, Node, Edge
from queue import PriorityQueue

from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def _init_(self, g: GraphInterface = None):
        self.graph = g
        self.INF = float('inf')

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name, 'r') as file:
            J = json.load(file)
            ListNode = J['Nodes']
            ListEdge = J['Edges']
        g = DiGraph()
        for n in ListNode:
            try:
                pos = n['pos']
                pos = tuple(pos.split(','))

            except Exception:
                x = random.uniform(35.19, 35.22)
                y = random.uniform(32.05, 32.22)
                pos = (x, y, 0.0)
            no = Node(Id=n['id'], pos=pos)
            i = no.get_id()
            g.add_node(i, pos)
            # self.graph.add_node(n['id'], pos)

        for e in ListEdge:
            ed = Edge(src=e['src'], dest=e["dest"], weight=e['w'])
            s = ed.getSrc()
            d = ed.getDest()
            w = ed.getWeight()
            g.add_edge(s, d, w)

        self.graph = g
        return True

    def save_to_json(self, file_name: str) -> bool:
        if self.graph is None:
            return False
        dict_ans = {"Edges": [], "Nodes": []}
        for n in self.graph.NodeDict.values():
            node_dict = {"id": n.id}
            if n.pos is not None:
                node_dict["pos"] = n.pos_to_string()
            dict_ans["Nodes"].append(node_dict)
            for e in self.graph.all_out_edges_of_node(n.id):
                w = str(self.graph.all_out_edges_of_node(n.id)[e].weight)
                edges_dict = {"src": n.id, "w": w, "dest": e}

                dict_ans["Edges"].append(edges_dict)
        try:
            print("dict:", dict_ans)
            with open(file_name, 'w') as writer:
                writer.write(json.dumps(dict_ans))
                return True
        except:
            print("error")
            return False
        finally:
            writer.close()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        node1 = self.graph.get_node(id1)
        node2 = self.graph.get_node(id2)
        node_list = self.graph.get_nodeList()
        self.reset(node_list)
        pr_queue = PriorityQueue()
        node1.set_weight(0)
        pr_queue.put((0, node1))
        visit_dict = self.update_visit(node_list)
        path = []
        while not pr_queue.empty():
            (dist, node1) = pr_queue.get()
            visit_dict[node1.get_id()] = True
            node_dict = self.graph.all_out_edges_of_node(node1.get_id())
            for i in node_dict:
                curr: Node = self.graph.get_node(i)
                distance = self.graph.all_out_edges_of_node(node1.get_id())[i].getWeight()
                # new_w = self.graph.all_out_edges_of_node(node1.get_id()).getWeight() + node1.get_weight()
                # print(new_w)
                if visit_dict[curr.get_id()] == False:
                    old_cost = curr.get_weight()
                    new_cost = node1.get_weight() + distance
                    if new_cost < old_cost:
                        curr.set_weight(new_cost)
                        curr.set_prev(node1)
                        pr_queue.put((new_cost, curr))
        path = []
        node1 = self.graph.get_node(id1)
        node = node2
        while node != node1:
            path.append(node.get_id())
            node = node.get_prev()
        path.append(node1.get_id())
        path.reverse()
        return node2.get_weight(), path

    def update_visit(self, dic):  # to chek were i visited
        new_d = {}
        for id in dic:
            curr: Node = self.graph.get_node(id)
            new_d[curr.get_id()] = False
        return new_d

    def reset(self, dic):  # to reset
        for id in dic:
            curr: Node = self.graph.get_node(id)
            curr.set_tag(-1)
            curr.set_weight(self.INF)

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        path = []
        tempList = []
        mini = math.inf
        temp_key = -1
        len_path = 0
        temp_node = node_lst.pop(0)
        path.append(temp_node)
        while len(node_lst) > 0:
            for node in node_lst:
                dis, tempList = self.shortest_path(temp_node, node)
                if mini > dis:
                    mini = dis
                    temp_key = node_lst.index(node)
            temp_node = node_lst.pop(temp_key)
            path.append(temp_node)
            len_path = len_path + mini
            mini = math.inf
        return path, len_path

        # shortest_path, path = float('inf'), []
        # for i in node_lst:
        #     for j in node_lst:
        #         new_path_length, new_path = self.shortest_path(i, j)
        #         if new_path_length < shortest_path and len(new_path) == len(node_lst):
        #             shortest_path, path = new_path_length, new_path
        # return path, shortest_path

    def centerPoint(self) -> (int, float):
        super().centerPoint()

    def plot_graph(self) -> None:
        x = []
        y = []
        # Run on all Nodes
        for n in self.graph.NodeDict.values():
            src_x = float(n.pos[0])
            src_y = float(n.pos[1])

            for k in self.graph.all_in_edges_of_node(n.id):
                dest = self.graph.NodeDict.get(k)
                dest_x = float(dest.pos[0])
                dest_y = float(dest.pos[1])

                plt.annotate("", xy=(src_x, src_y), xytext=(dest_x, dest_y), arrowprops=dict(arrowstyle="->"))
            plt.annotate(n.id, (src_x, src_y))
            x.append(src_x)
            y.append(src_y)

        plt.title("Graph plot")
        plt.scatter(x, y, c='red')
        plt.show()


if __name__ == '_main_':
    algo = GraphAlgo()
    algo.load_from_json(r"../data/A1.json")

    # graph = DiGraph()
    # print(algo.graph)
    algo.plot_graph()
