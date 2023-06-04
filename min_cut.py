import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edge(0, 1, capacity=5)
G.add_edge(0, 3, capacity=14)
G.add_edge(1, 2, capacity=4)
G.add_edge(1, 4, capacity=5)
G.add_edge(1, 5, capacity=4)
G.add_edge(2, 5, capacity=3)
G.add_edge(3, 1, capacity=13)
G.add_edge(3, 6, capacity=5)
G.add_edge(3, 7, capacity=2)
G.add_edge(4, 3, capacity=6)
G.add_edge(4, 7, capacity=6)
G.add_edge(5, 4, capacity=4)
G.add_edge(5, 7, capacity=3)
G.add_edge(5, 8, capacity=6)
G.add_edge(6, 7, capacity=3)
G.add_edge(7, 8, capacity=12)

# Find the minimum cut
cut_value, partition = nx.minimum_cut(G, 0, 3)
reachable, non_reachable = partition

# Print the results
print("Minimum cut value:", cut_value)
print("Node set reachable from source:", reachable)
print("Node set not reachable from source:", non_reachable)
