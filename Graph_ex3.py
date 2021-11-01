import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge(0, 1)
G.add_edge(0, 4)
G.add_edge(0, 5)
G.add_edge(1, 6)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(2, 7)
G.add_edge(3, 4)
G.add_edge(3, 8)
G.add_edge(4, 5)
G.add_edge(4, 9)
G.add_edge(5, 7)
G.add_edge(6, 8)
G.add_edge(6, 9)
G.add_edge(0, 1)
G.add_edge(7, 9)

print(f"centro: {nx.center(G)}")
print(f"Graus: {G.degree}")
print(f"Número de nós: {nx.number_of_nodes(G)}")
print(f"Número de arestas: {nx.number_of_edges(G)}")
print(f"Centralidade dos nós: {nx.degree_centrality(G)}")
print(f"Dencidade dos nós: {nx.density(G)}")

nx.draw_networkx(G, with_labels=True)

ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()