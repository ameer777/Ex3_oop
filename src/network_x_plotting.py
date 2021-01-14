import matplotlib.pyplot as plt
import networkx as nx


def network_x_plot(g):
    G = nx.DiGraph()
    edges = set()
    for src in g.get_edges():
        for dest in g.get_edges()[src]:
            edges.add(g.get_edges()[src][dest])
    for edge in edges:
        G.add_edges_from([(edge.getSrc(), edge.getDest())], weight=edge.getWeight())
    v_blue = []
    edges = []
    for i in range(len(G.nodes)):
        v_blue.append('blue')
    for i in G.edges():
        edges.append(i)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                           node_color=v_blue, node_size=300)
    nx.draw_networkx_edges(G, pos, edgelist=edges, arrows=True)
    nx.draw_networkx_labels(G, pos)
    plt.show()