from src.EdgeData import EdgeData
from src.NodeData import NodeData
from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        self.edges = {}
        self.graph = {}
        self.MC = 0
        self.edgeSize = 0


    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return len(self.graph.keys())


    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.edgeSize

    def get_edges(self):
        return self.edges

    def get_nodes(self):
        return self.graph

    def load_graph(self, edges, nodes, edgeSize):
        self.edges = edges
        self.graph = nodes
        self.edgeSize = edgeSize

    def getNode(self, key):
        if key in self.graph:
            return self.graph[key]
        return None

    def getEdge(self, src, dest):
        if src in self.graph and dest in self.graph and src != dest and src in self.edges and dest in self.edges[src]:
            return self.edges[src][dest]
        return None


    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """
        if self.graph is not None:
            return self.graph.values()
        return None


    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        node = self.getNode(id1)
        return node.getInEdges()


    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        if id1 in self.edges.keys() and self.edges[id1].values() is not None:
            return self.edges[id1].values()
        return {}


    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.MC


    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if id1 == id2 or weight < 0:
            return False
        if id1 in self.graph and id2 in self.graph:
            if self.getEdge(id1, id2) is None:
                self.edgeSize += 1
            self.MC += 1
            edge = EdgeData(id1, id2, weight)
            if id1 not in self.edges:
                self.edges[id1] = {}
            self.edges[id1][id2] = edge
        self.getNode(id1).addOutEdge(edge)
        self.getNode(id2).addInEdge(edge)
        return True



    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        node = self.getNode(node_id)
        if node is not None:
            return False
        else:
            node = NodeData(node_id, pos)
            self.graph[node_id] = node
            self.MC += 1
            return True


    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        if node_id not in self.graph:
            return False
        node = self.getNode(node_id)
        in_edges = node.getInEdges()

        for edge in in_edges:
            self.remove_edge(edge.getSrc(), node_id)
            self.edgeSize -= 1
        if node_id in self.edges:
            count = len(self.edges[node_id])
            del self.edges[node_id]
        else:
            count = 0
        self.edgeSize -= count
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        if node_id1 in self.graph and node_id2 in self.graph and self.getEdge(node_id1, node_id2) is not None:
            self.edgeSize -= 1
            self.MC += 1
            del self.edges[node_id1][node_id2]
            return True
        return False
