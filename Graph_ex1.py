import networkx as nx
import matplotlib.pyplot as plt

K5 = nx.complete_graph(5)

nx.draw_circular(K5)

ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()