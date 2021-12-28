import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestDiGraph(unittest.TestCase):

    def test_load_from_json(self):
        ga = GraphAlgo()
        self.assertTrue(ga.load_from_json("C:/Users/adi.fin45/PycharmProjects/Ex3/data/10000Nodes.json"))

    def test_save_from_json(self):
        graphAlgo = GraphAlgo(DiGraph())
        graphAlgo.load_from_json("C:/Users/adi.fin45/PycharmProjects/Ex3/data/A2.json")
        self.assertTrue(graphAlgo.save_to_json("temp.json"))

    def test_shortest_path(self):
        graphAlgo = GraphAlgo(DiGraph())
        graphAlgo.graph.add_node(0)
        graphAlgo.graph.add_node(1)
        graphAlgo.graph.add_node(2)
        graphAlgo.graph.add_edge(0, 1, 1)
        graphAlgo.graph.add_edge(1, 2, 4)
        self.assertEqual(graphAlgo.shortest_path(0, 1), (1, [0, 1]))
        self.assertEqual(graphAlgo.shortest_path(0, 2), (5, [0, 1, 2]))

    def test_all_in_edges_of_node(self):
        graphAlgo = GraphAlgo()
        graphAlgo.load_from_json("C:/Users/adi.fin45/PycharmProjects/Ex3/data/A1.json")
        self.assertEqual(len(graphAlgo.graph.all_in_edges_of_node(0)), 2)

    def test_all_out_edges_of_node(self):
        graphAlgo = GraphAlgo()
        graphAlgo.load_from_json("C:/Users/adi.fin45/PycharmProjects/Ex3/data/A1.json")
        self.assertEqual(len(graphAlgo.graph.all_out_edges_of_node(0)), 2)

    def test_get_mc(self):
        graphAlgo = GraphAlgo()
        graphAlgo.load_from_json("C:/Users/adi.fin45/PycharmProjects/Ex3/data/A1.json")
        self.assertEqual(graphAlgo.graph.get_mc(), 53)

    def test_TSP(self):
        g_algo = GraphAlgo()
        file1 = '../data/A0.json'
        file2 = '../data/A1.json'
        g_algo.load_from_json(file1)
        cities = []
        for n in g_algo.graph.NodeDict.values():
            cities.append(n.id)
        self.assertEqual(g_algo.TSP(cities), ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 14.470852790366884))
        g_algo.load_from_json(file2)
        cities = []
        for n in g_algo.graph.NodeDict.values():
            cities.append(n.id)
        self.assertEqual(g_algo.TSP(cities),
                         ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 22.63446693792369))

        # graphAlgo = GraphAlgo()
        # graphAlgo.load_from_json("C:/Users/adi.fin45/PycharmProjects/Ex3/data/A2.json")
        # path = [7, 8, 35, 33, 32, 5]
        # expected = ([8, 7, 6, 5, 6, 2, 32, 33, 34, 35], 12.82175466200503)
        # self.assertEqual(expected, graphAlgo.TSP(path))

        # g = DiGraph()
        # g.add_node(1)
        # g.add_node(2)
        # g.add_node(3)
        # g.add_node(4)
        # g.add_node(5)
        # g.add_edge(1, 2, 3)
        # g.add_edge(1, 3, 5)
        # g.add_edge(3, 2, 4)
        # g.add_edge(2, 5, 7)
        # g.add_edge(4, 1, 3)
        # g.add_edge(5, 2, 4)
        # g.add_edge(3, 1, 9)
        # g.add_edge(3, 4, 2)
        # g.add_edge(5, 1, 2)
        # algo_g = GraphAlgo(g)
        # cities = [3, 5, 1, 2]
        # ans = algo_g.TSP(cities)
        # self.assertEqual(ans, ([3, 2, 5, 1], 13))


if __name__ == '__main__':
    unittest.main()
