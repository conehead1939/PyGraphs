import networkx as nx
import matplotlib.pyplot as plt
import random

# Function to generate a directed graph with random weights
def generer_graphe_oriente(n):
    # Création du graphe orienté
    G = nx.DiGraph()
    
    # Ajouter des nœuds nommés de x0 à xn
    for i in range(n):
        G.add_node(f"x{i}")
    
    # Ajouter des arêtes avec des poids aléatoires entre 1 et 100, uniquement dans une direction
    for i in range(n):
        for j in range(i + 1, n):  # Évite les doublons d'arcs en sens inverse
            if random.choice([True, False]):  # Choisir aléatoirement une direction
                poids = random.randint(1, 100)
                G.add_edge(f"x{i}", f"x{j}", weight=poids)
            else:
                poids = random.randint(1, 100)
                G.add_edge(f"x{j}", f"x{i}", weight=poids)
    
    return G

# Function to display the graph with an optional path highlighted
def afficher_graphe(G, chemin=None):
    pos = nx.spring_layout(G)
    
    # Dessiner le graphe avec des flèches et les poids des arêtes
    nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", arrows=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    # Si un chemin est fourni, colorier les arêtes du chemin
    if chemin:
        edges = [(chemin[i], chemin[i+1]) for i in range(len(chemin)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2, arrows=True)

    plt.show()

# Function to apply Bellman-Ford algorithm and return the shortest path
def bellman_ford_graphe(G, source, target):
    # Calculer les distances et le chemin le plus court avec Bellman-Ford
    try:
        distance = nx.single_source_bellman_ford_path_length(G, source)
        chemin = nx.single_source_bellman_ford_path(G, source)[target]
        return chemin, distance[target]
    except nx.NetworkXNoPath:
        return None, None

# Main function that combines everything
def run_bellman_ford(num_vertices, source, target):
    # Generate the directed graph
    G = generer_graphe_oriente(num_vertices)
    
    # Display the generated graph
    afficher_graphe(G)
    
    # Apply Bellman-Ford and get the results
    chemin, distance = bellman_ford_graphe(G, source, target)
    afficher_graphe(G, chemin)
    return chemin, distance
    