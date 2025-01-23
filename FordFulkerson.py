import networkx as nx
import random
import matplotlib.pyplot as plt
from collections import deque

def generer_graphe_oriente_avec_capacites(n):
    # Create a directed graph with random capacities
    G = nx.DiGraph()
    
    # Add nodes and edges with random capacities
    for i in range(n):
        G.add_node(f"x{i}")
        
    for i in range(n):
        for j in range(i + 1, n):  # Avoid reverse edges (ensure one-way)
            if random.choice([True, False]):
                capacite = random.randint(1, 100)
                G.add_edge(f"x{i}", f"x{j}", capacity=capacite)
    
    return G

def bfs_residuel(G, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        u = queue.popleft()
        
        for v in G.neighbors(u):
            if v not in visited and G[u][v]['capacity'] > 0:  # Available capacity
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

def ford_fulkerson(G, source, sink):
    # Copy graph for residual capacities
    residual_graph = G.copy()
    parent = {}
    max_flow = 0
    
    # Augment the flow while there is an augmenting path
    while bfs_residuel(residual_graph, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s]['capacity'])
            s = parent[s]
        
        # Update residual capacities of edges and reverse edges
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v]['capacity'] -= path_flow
            if residual_graph.has_edge(v, u):
                residual_graph[v][u]['capacity'] += path_flow
            else:
                residual_graph.add_edge(v, u, capacity=path_flow)
            v = parent[v]
        
        max_flow += path_flow
    
    return max_flow

def afficher_graphe(G, flow=None):
    pos = nx.spring_layout(G)
    
    # Draw the graph with node labels
    nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", arrows=True)
    
    # Draw the edge labels (capacities)
    edge_labels = nx.get_edge_attributes(G, 'capacity')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # If there's flow, color the flow edges
    if flow:
        flow_edges = [(u, v) for u, v, d in flow if d > 0]
        nx.draw_networkx_edges(G, pos, edgelist=flow_edges, edge_color='green', width=2)
    
    plt.show()