import json
import random
from turtledemo.chaos import g
from typing import List, Type, Any

from src import GraphInterface
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: GraphInterface = DiGraph()):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name, 'r') as file:
            J = json.load(file)
            ListNode = J['Nodes']
            ListEdge = J['Edges']
        for n in ListNode:
            try:
                pos = n['pos']
            except Exception:
                x = random.uniform(35.19, 35.22)
                y = random.uniform(32.05, 32.22)
                pos = (x, y, 0.0)

            self.graph.add_node(n['id'], pos)
        for e in ListEdge:
            self.graph.add_edge(e['src'], e['dest'], e['w'])
        return True

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        super().centerPoint()

    def plot_graph(self) -> None:
        pass
