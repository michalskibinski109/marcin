import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx
from itertools import combinations


def create_random_edges(G, k):
    """
    Creates edges between nodes in a graph based on the type of connection
    G: networkx graph
    k: int probability of creating an edge
    """
    pairs = list(combinations(G.nodes(), 2))
    edges = []
    nodes = list(G.nodes())
    for pair in pairs:
        if np.random.random() <= k:
            edges.append(pair)
    G.remove_edges_from(G.edges)
    G.add_edges_from(edges)

    return G


def spread(G, infected_nodes, k):
    """
    G: networkx graph
    infected_nodes: list of nodes
    k: probability of infecting a node
    """
    new_infected_nodes = []
    for node in infected_nodes:
        neighbors = list(G.neighbors(node))
        for node in G.nodes:
            if node in neighbors and np.random.random() < k:
                new_infected_nodes.append(node)
    print(new_infected_nodes)
    return list(set(infected_nodes + new_infected_nodes))


class AnimatedPlot:
    def __init__(self, G, infected_nodes, spread_func, k=1):
        self.G = G
        self.N = len(G)
        self.pos = nx.spring_layout(G)
        self.infected_nodes = infected_nodes
        self.fig, self.ax = plt.subplots(figsize=(9, 7))
        self.k = k
        self.real_iterations = 0
        self.spread_func = spread_func

    def update(self, num):
        if len(self.infected_nodes) == self.N:
            self.ax.set_title(
                f"All nodes infected in {self.real_iterations} iterations"
            )
            return
        self.ax.clear()

        if num > 0:
            self.infected_nodes = self.spread_func(self.G, self.infected_nodes, self.k)
        nx.draw(
            self.G,
            pos=self.pos,
            ax=self.ax,
            with_labels=True,
            node_color="blue",
            edge_color="red",
        )
        nx.draw_networkx_nodes(
            self.G,
            pos=self.pos,
            ax=self.ax,
            nodelist=self.infected_nodes,
            node_color="red",
        )
        self.real_iterations = num
        self.ax.set_title(f"Iteration {num + 1}")
        self.ax.legend(["Healthy", "", "Infected"])

    def __call__(self, frames=10, interval=1000):
        ani = animation.FuncAnimation(
            self.fig, self.update, frames=frames, interval=interval, repeat=False
        )
        plt.show()


if __name__ == "__main__":
    np.random.seed(42)
    G = nx.Graph()
    G.add_nodes_from(range(25))
    G = create_random_edges(G, 0.156)
    ani = AnimatedPlot(G, [0], spread, 1)
    ani(10, 1000)
