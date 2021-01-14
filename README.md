# Ex3_oop

## Ex3 contains the following classes:
* NodeData - representing a vertex in the graph.
* EdgeData - representing a edge in the graph.
* DiGraph- implementing GraphInterface- representing a directed weighted graph.
* GraphAlgo- implementing GraphAlgoInterface interface.

## Graph implementation
DiGraph class represents a directed weighted graph, represented by a dictionary.
The reason we chose to represent the graph in a dictionary is because it allows easy access to each node in the graph, therefor questions like whether two nodes are connected and how many edges are in the graph can be answered in O(1). Adding a new node to the graph, or connecting two nodes in the graph with an edge, can also be done easily in O(1). Connecting simply requires adding each of the nodes to the other node's neighbors list with the wanted weight, and removing an edge requires removing each of the nodes from the other node's neighbors list.

### the basic functions in graph :
* __add node__ - add a new node to the graph
* __add_edge__ - add a new edge to the graph between two vertices
* __get_all_ v__ - return a dictionary contains all the graph vertices
* __remove node__ - remove a vertex from the graph
* __remove edge__ - remove an edge between two vertices
* __all_in_edges_of_node__ - returns a dictionary of all nodes connected to the given node.
* __all_out_edeges_of_node__ - returns a dictionary of all nodes connected from the given node.
* __e_size__ - return the number of edges in the graph
* __v_size__ - returns the number of vertices in the graph
* __get_mc__ - return the number of changes computed on the graph

__the graph class includes functions such as:__

__def __init __(self):__
this method initilizes a new directed weighted graph.

__def v_size(self) -> int:__
this method returns the number of nodes in the graph.

__def e_size(self) -> int:__
this method returns the number of edges in the graph

__def get_all_v(self) -> dict:__ 
this method returns a dict with all the nodes in the graph, with the ID of each node ass the key and the node_data itself as the value.

__def get_all_v(self) -> dict:__ 
this method returns a dict with all the nodes in the graph, with the ID of each node ass the key and the node_data itself as the value.

__def all_in_edges_of_node(self, id1: int) -> dict:__ 
this method returns a dict contains all the edges that comming to the given node.

__def add_edge(self, id1: int, id2: int, weight: float) -> bool:__
this method connect between the two given nodes with the given weight.
if the weight is not positive, or if there is already an edge between the two nodes, or if one of them does not exist in the graph, the method does nothing and simply returns false.
else, the method add the ID of the src node to the outedges dictionary of the graph, and add the ID of the dest to the Inedges dictionary of the graph.
returns true.

__def add_node(self, node_id: int, pos: tuple = None) -> bool:__
this nethod creates a new node with the given id, and add it to the graph.
it creates a new inner dictionery for each of the edge list for the new node, and returns true.

__def remove_node(self, node_id: int) -> bool:__
this method removes the node woth the given ID from the graph, and delete all its edges, coming out andd comming in.
first, the method delete the node from the nodes dictionary, and then runs on each of its neighbors and pop the node from the list of neighbors of its neighbors.
if the node removed successfully, the method returns true.
if there is no such node the method returns false and simply does nothing.

__def remove_edge(self, node_id1: int, node_id2: int) -> bool:__
this method removes the edge between the two given nodes from the graph.
if there is no such edge, or one of the nodes does not exist, the method returns false and does nothing
delede from the dictionery of the inner edges the src node,and delede from the dictionery of the out edges the dest node,
returns true.


## Algorithms

__GraphAlgo__ class represents the regular Graph Theory algorithms including:

* __load_from_json(file)
* __save_to_json(file)
* __shortestPath(int src, int dest) -> (float, list)
* __connected_component(node_id) -> list
* __connected_components() -> List[list]
* __plot_graph()

### The Dijkstra algorithm


