
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("edges.csv")

railway_graph = nx.Graph()

for index, row in df.iterrows():
    railway_graph.add_edge(row["from"], row["to"])

nx.draw_spectral(railway_graph, with_labels=True)
plt.show()


