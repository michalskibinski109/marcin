import networkx as nx
import numpy as np


def create_edges(G: nx.Graph, type_of_connection: str) -> nx.Graph:
    """
    Creates edges between nodes in a graph based on the type of connection
    args:
        G: networkx graph
        type_of_connection: str
        - linear
        - random
        - grid
        - complete
        - star
    """
    edges = []
    nodes = list(G.nodes())
    if type_of_connection == "linear":
        for i in range(len(nodes) - 1):
            edges.append((nodes[i], nodes[i + 1]))
    elif type_of_connection == "grid":
        for i in range(len(nodes)):
            if i % 2 == 0 and i + 1 < len(nodes):
                edges.append((nodes[i], nodes[i + 1]))
            else:
                edges.append((nodes[i], nodes[i - 1]))
    elif type_of_connection == "random":
        for i in range(len(nodes) - 1):
            edges.append((nodes[i], np.random.choice(nodes)))
    elif type_of_connection == "complete":
        for i in range(len(nodes) - 1):
            for j in range(i + 1, len(nodes)):
                edges.append((nodes[i], nodes[j]))
    elif type_of_connection == "star":
        for i in range(1, len(nodes)):
            edges.append((nodes[0], nodes[i]))
    else:
        raise ValueError("Unknown type of connection")
    G.add_edges_from(edges)
    return G
