import unittest

from src.DiGraph import DiGraph


class MyTestCase(unittest.TestCase):

    def test_removeEdge(self):
        my_graph = DiGraph()
        my_graph.add_node(1, 3)
        my_graph.add_node(2, 3)
        my_graph.add_node(3, 3)
        my_graph.add_node(4, 3)
        my_graph.add_edge(1, 2, 3)
        my_graph.add_edge(2, 3, 3)
        my_graph.add_edge(3, 4, 3)


        self.assertEqual(True, my_graph.remove_edge(2, 3))
        self.assertEqual(False, my_graph.remove_edge(2, 3))

    def test_removeNode(self):
        my_graph = DiGraph()
        my_graph.add_node(1, 3)
        my_graph.add_node(2, 3)
        my_graph.add_node(3, 3)
        my_graph.add_node(4, 3)
        my_graph.add_edge(1, 2, 3)
        my_graph.add_edge(2, 3, 3)
        my_graph.add_edge(3, 4, 3)
        self.assertEqual(True, my_graph.remove_node(4))


if __name__ == '__main__':
    unittest.main()
