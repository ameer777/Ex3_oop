from typing import List
import json
import os
import matplotlib.pyplot as plt
from numpy import random
from pathlib import Path
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph=None):
        if graph is None:
            self.directed_weighted_graph = DiGraph()
        else:
            self.directed_weighted_graph = graph
        self.parent = {}
        self.dis = {}

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.directed_weighted_graph

    def parse_file_name(self, file_name):
        file_name = file_name.replace('/', '\\')
        file_name = file_name.replace('\\\\', '\\')
        file_name = file_name.split('\\')
        base_path = Path(__file__).parent.parent
        file_path = ""
        for i in range(len(file_name) - 1):
            if not file_name[i].startswith('..'):
                file_path += file_name[i] + '/'
        file_path = (base_path / file_path / file_name[len(file_name) - 1]).resolve()
        return file_path

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        file_path = self.parse_file_name(file_name)

        with open(file_path, 'r') as fp:
            data = json.load(fp)

        nodes = data["Nodes"]
        edges = data["Edges"]

        for n in nodes:
            if "pos" in n:
                pos = n['pos']
                if type(pos) == str:
                    pos = tuple(pos.split(','))
                pos = (float(pos[0]), float(pos[1]))
                self.directed_weighted_graph.add_node(n["id"], pos)
            else:
                self.directed_weighted_graph.add_node(n["id"])
        for e in edges:
            self.directed_weighted_graph.add_edge(e["src"], e["dest"], e["w"])
        return True

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        file_name = self.parse_file_name(file_name)
        try:
            os.remove(file_name)
        except OSError:
            pass

        edges = self.directed_weighted_graph.get_edges()
        nodes = self.directed_weighted_graph.get_nodes()
        json_file = {}
        jsonEdges = []
        jsonNodes = []

        for src in edges:
            for dest in edges[src]:
                edge = edges[src][dest]
                parsed_edge = {'src': edge.getSrc(), 'dest': edge.getDest(), 'w': edge.getWeight()}
                jsonEdges.append(parsed_edge)

        for k in nodes:
            if nodes[k].getLocation():
                pos = nodes[k].getLocation()
                parsed_node = {'pos': pos, 'id': k}
            else:
                parsed_node = {'id': k}
            jsonNodes.append(parsed_node)

        json_file["Edges"] = jsonEdges
        json_file["Nodes"] = jsonNodes
        with open(file_name, 'x') as fp:
            json.dump(json_file, fp)
            return True

    def shortest_path_dist(self, src: int, dest: int) -> float:
        if src == dest:
            return 0
        self.dijkstra(self.directed_weighted_graph.getNode(src))
        return self.dis[dest]

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        if self.directed_weighted_graph.getNode(id1) is None or self.directed_weighted_graph.getNode(id2) is None:
            return None

        self.dijkstra(self.directed_weighted_graph.getNode(id1))
        s = self.directed_weighted_graph.getNode(id2)
        path = []
        while s is not None:
            path.append(s.getKey())
            s = self.parent[s.getKey()]
        path.reverse()
        weight = self.dis[id2]
        if weight == float('inf'):
            return weight, []
        return weight, path

    """
    function Dijkstra(Graph, source):

    create vertex set Q

    for each vertex v in Graph:             // Initialization
        dist[v] ← INFINITY                  // Unknown distance from source to v
        prev[v] ← UNDEFINED                 // Previous node in optimal path from source
        add v to Q                          // All nodes initially in Q (unvisited nodes)

    dist[source] ← 0                        // Distance from source to source

    while Q is not empty:
        u ← vertex in Q with min dist[u]    // Node with the least distance will be selected first
        remove u from Q 

        for each neighbor v of u:           // where v is still in Q.
            alt ← dist[u] + length(u, v)
            if alt < dist[v]:               // A shorter path to v has been found
                dist[v] ← alt 
                prev[v] ← u 

    return dist[], prev[]
    """

    def dijkstra(self, src):
        self.dis = {}
        self.parent = {}
        visited = set()
        q = []
        for n in self.directed_weighted_graph.get_all_v():
            self.dis[n.getKey()] = float('inf')
            self.parent[n.getKey()] = None
        self.dis[src.getKey()] = float(0)
        q.append((src.getKey(), 0))
        while len(q) > 0 and len(visited) != self.directed_weighted_graph.v_size():
            key = q.pop(0)[0]
            if key not in visited:
                for v in self.directed_weighted_graph.getNode(key).getOutEdges():
                    if v.getDest() not in visited:
                        if self.directed_weighted_graph.getEdge(key, v.getDest()) is not None:
                            tempSum = self.dis[key] + self.directed_weighted_graph.getEdge(key, v.getDest()).getWeight()
                            if tempSum < self.dis[v.getDest()]:
                                self.dis[v.getDest()] = tempSum
                                self.parent[v.getDest()] = self.directed_weighted_graph.getNode(key)
                            q.append((v.getDest(), self.dis[v.getDest()]))
                            sorted(q, key=lambda n: n[1])
            visited.add(key)

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        Notes:
        If the graph is None or id1 is not in the graph, the function should return an empty list []
        """
        list = []
        if self.directed_weighted_graph.getNode(id1) is None:
            return list

        list.append(id1)
        for n in self.directed_weighted_graph.get_all_v():
            if self.shortest_path(n.getKey(), id1)[0] != float('inf') and self.shortest_path(id1, n.getKey())[0] != float('inf'):
                if n.getKey() is not id1:
                    list.append(n.getKey())
        return list

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        Notes:
        If the graph is None the function should return an empty list []
        """
        lists = []
        if self.directed_weighted_graph is None:
            return lists

        for n in self.directed_weighted_graph.get_all_v():
            lists.append(self.connected_component(n.getKey()))

        return lists

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        ax = plt.axes()
        min_x = float('inf')
        max_x = -float('inf')
        min_y = float('inf')
        max_y = -float('inf')
        for node in self.directed_weighted_graph.get_nodes():
            mynode = self.directed_weighted_graph.getNode(node)
            node_pos = mynode.getLocation()
            if node_pos is not None:
                if node_pos[0] < min_x:
                    min_x = node_pos[0]
                if node_pos[1] < min_y:
                    min_y = node_pos[1]
                if node_pos[0] > max_x:
                    max_x = node_pos[0]
                if node_pos[1] > max_y:
                    max_y = node_pos[1]
            else:
                min_x, max_x, min_y, max_y = 0, 500, 0, 500

        plt.xlim(min_x + (min_x * 0.59), max_x + (max_x * 0.59))
        plt.ylim(min_y + (min_y * 0.59), (max_y * 0.59) + max_y)

        edges = self.directed_weighted_graph.get_edges()
        plotted = []
        circles = []
        for src in edges:
            src_node = self.directed_weighted_graph.getNode(src)
            for dest in edges[src]:
                dest_node = self.directed_weighted_graph.getNode(dest)
                src_pos = src_node.getLocation()
                dest_pos = dest_node.getLocation()
                if src_pos is None:
                    src_pos = [random.uniform(min_x, max_x), random.uniform(min_y, max_y)]
                    src_node.setLocation(src_pos[0], src_pos[1])
                if dest_pos is None:
                    dest_pos = [random.uniform(min_x, max_x), random.uniform(min_y, max_y)]
                    dest_node.setLocation(dest_pos[0], dest_pos[1])
                c1 = plt.Circle((src_pos[0], src_pos[1]), max_x / 100 + max_y / 100, color='r')
                c2 = plt.Circle((dest_pos[0], dest_pos[1]), max_x / 100 + max_y / 100, color='r')
                if c1 not in circles:
                    circles.append(c1)
                if c2 not in circles:
                    circles.append(c2)

                if (src_pos[0] == dest_pos[0] and src_pos[1] == dest_pos[1]):
                    dest_pos = (dest_pos[0] + 0.1, dest_pos[1] + 0.1)
                plt.arrow(src_pos[0], src_pos[1], dest_pos[0] - src_pos[0], dest_pos[1] - src_pos[1],
                          head_width=max_x * 0.039,
                          length_includes_head=True,
                          head_length=max_y * 0.039, width=max_y * 0.00002 * max_y,
                          color='black', fc="tan")

                plt.title('|V|=' + str(self.directed_weighted_graph.v_size()) + ',' + '|E|= ' + str(
                    self.directed_weighted_graph.e_size()) + ')',
                          fontdict={'color': 'white', 'fontsize': 19, 'fontweight': 980})
                if (src_pos[0], src_pos[1]) not in plotted:
                    label = ax.annotate(src_node.getKey(), xy=(src_pos[0], src_pos[1]), fontsize=15)
                    plotted.append([src_pos[0], src_pos[1]])
                if (dest_pos[0], dest_pos[1]) not in plotted:
                    label = ax.annotate(dest_node.getKey(), xy=(dest_pos[0], dest_pos[1]), fontsize=15)
                    plotted.append([dest_pos[0], dest_pos[1]])

        for i in circles:
            ax.add_artist(i)

        plt.show()

