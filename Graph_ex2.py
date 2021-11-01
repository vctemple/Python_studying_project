import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([('A','B'), ('B','C'), ('A','C')])

G.add_node('D')

G.add_edge('D', 'A')
G.add_edge('D', 'B')
G.add_edge('D', 'C')

nx.draw_circular(G, with_labels=True)

ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()