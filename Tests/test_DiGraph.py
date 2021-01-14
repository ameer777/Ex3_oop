import unittest

from src.DiGraph import DiGraph

class DiGraph_testing(unittest.TestCase):

    def test_init_graph(self):
        print("test_init_graph")
        graph = DiGraph()
        mc = graph.get_mc()
        edges = graph.get_edges()
        nodes = graph.get_nodes()
        edge_size = graph.e_size()
        node_size = graph.v_size()
        self.assertEqual(mc, 0)
        self.assertEqual(edge_size, 0)
        self.assertEqual(node_size, 0)
        self.assertIsInstance(edges, dict)
        self.assertIsInstance(nodes, dict)

    def test_get_nodes(self):
        print("test_get_nodes")
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        nodes = graph.get_nodes()
        self.assertIsNotNone(nodes)
        self.assertTrue(len(nodes), 4)
        self.assertEqual(nodes[1].getKey(), 1)
        self.assertEqual(nodes[2].getKey(), 2)
        self.assertEqual(nodes[3].getKey(), 3)
        self.assertEqual(nodes[4].getKey(), 4)

    def test_get_edges(self):
        print("test_get_edges")
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_edge(1, 2, 1)
        graph.add_edge(1, 3, 2)
        graph.add_edge(3, 1, 3)
        edges = graph.get_edges()
        self.assertIsNotNone(edges)
        self.assertIsNotNone(edges[1])
        self.assertIsNotNone(edges[3])
        self.assertIsNotNone(edges[1][2])
        self.assertIsNotNone(edges[1][2])
        self.assertIsNotNone(edges[3][1])
        e1 = edges[1][2]
        e2 = edges[1][3]
        e3 = edges[3][1]
        self.assertTrue(e1.getWeight(), 1)
        self.assertTrue(e2.getWeight(), 2)
        self.assertTrue(e3.getWeight(), 3)

    def test_remove_node(self):
        print("test_remove_node")
        graph = DiGraph()
        graph.add_node(0)
        self.assertTrue(len(graph.get_nodes()), 1)
        graph.remove_node(0)
        self.assertTrue(len(graph.get_nodes()), 0)

    def test_remove_edge(self):
        print("test_remove_edge")
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_edge(0, 1, 1)
        self.assertTrue(len(graph.get_edges()), 1)
        graph.remove_edge(0, 1)
        self.assertTrue(len(graph.get_edges()), 0)

    def test_getNode_getEdge(self):
        print("test_getNode_getEdge")
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_edge(0, 1, 1)
        e = graph.getEdge(0, 1)
        self.assertIsNotNone(e)
        self.assertEqual(e.getSrc(), 0)
        self.assertEqual(e.getDest(), 1)
        self.assertEqual(e.getWeight(), 1)
        n = graph.getNode(0)
        self.assertIsNotNone(n)
        self.assertEqual(n.getKey(), 0)


if __name__ == '__main__':
    unittest.main()
