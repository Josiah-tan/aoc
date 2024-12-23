from collections import deque
from typing import DefaultDict



file_number = 1
part_1 = True
# from competitive import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    entries = [i.split("-") for i in f.read().rstrip().split('\n')]
print(f"entries = {entries}")


graph = DefaultDict(set)

for a, b in entries:
    graph[a].add(b)
    graph[b].add(a)


sets = set()

def dfs(history, node, depth):
    if depth == 3:
        for next_node in graph[node]:
            if next_node == history[0]:
                sets.add(tuple(sorted(history)))
    else:
        for next_node in graph[node]:
            dfs(history + [next_node], next_node, depth + 1)



for item in graph.keys():
    history = [item]
    dfs(history, item, 1)

print(f"sets = {sets}")

answer_1 = 0
for s in sets:
    possibility = False
    for a in s:
        possibility |= a.startswith("t")
    answer_1 += possibility

print(f"answer_1 = {answer_1}")


##

import networkx as nx

# Parse the input into edges
file_number = 2
part_1 = True
# from competitive import Point, sign
# import numpy as np
with open(f'{file_number}.txt') as f:
    edges = f.read().rstrip().split('\n')


# Create an undirected graph
G = nx.Graph()
for edge in edges:
    node1, node2 = edge.split('-')
    G.add_edge(node1, node2)

# Find all maximal cliques
cliques = list(nx.find_cliques(G))

# Find the largest clique
largest_clique = max(cliques, key=len)

# Sort alphabetically and join with commas
password = ",".join(sorted(largest_clique))

print("Password to the LAN party:", password)

