import unittest
from src.GraphAlgo import GraphAlgo
import os


class GraphAlgo_test(unittest.TestCase):

    def test_init(self):
        print("test_init")
        g_algo = GraphAlgo()
        graph = g_algo.get_graph()
        self.assertIsNotNone(g_algo)
        self.assertIsNotNone(graph)

    def test_json(self):
        print("test_json")
        g_algo = GraphAlgo()
        graph = g_algo.get_graph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 2, 2)
        g_algo.save_to_json("test_file")
        g_algo = GraphAlgo()
        g_algo.load_from_json("test_file")
        graph = g_algo.get_graph()
        nodes = list(graph.get_all_v())
        edge1 = graph.getEdge(0, 1)
        edge2 = graph.getEdge(1, 2)
        self.assertIsNotNone(edge1)
        self.assertIsNotNone(edge2)
        self.assertIsNotNone(nodes[0])
        self.assertIsNotNone(nodes[1])
        self.assertIsNotNone(nodes[2])
        self.assertEqual(edge1.getWeight(), 1)
        self.assertEqual(edge2.getWeight(), 2)
        try:
            os.remove(g_algo.parse_file_name("test_file"))
        except OSError:
            pass

    def test_shortest_path(self):
        print("test_shortest_path")
        g_algo = GraphAlgo()
        graph = g_algo.get_graph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 2, 1)
        graph.add_edge(2, 3, 1)
        graph.add_edge(3, 4, 1)
        graph.add_edge(0, 4, 3)
        d = g_algo.shortest_path_dist(0, 4)
        l = g_algo.shortest_path(0, 4)
        self.assertIsNotNone(d)
        self.assertEqual(d, 3)
        self.assertIsNotNone(l)
        self.assertEqual(l[0], 3.0)
        self.assertEqual(l[1], [0,4])

    def test_connected_component(self):
        print("test_connected_component")
        g_algo = GraphAlgo()
        graph = g_algo.get_graph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 2, 1)
        graph.add_edge(2, 3, 1)
        graph.add_edge(3, 4, 1)
        graph.add_edge(0, 4, 3)
        l = g_algo.connected_components()
        self.assertIsNotNone(l)
        self.assertEqual(l[0], [0])
        self.assertEqual(l[1], [1])
        self.assertEqual(l[2], [2])
        self.assertEqual(l[3], [3])
        self.assertEqual(l[4], [4])


if __name__ == '__main__':
    unittest.main()