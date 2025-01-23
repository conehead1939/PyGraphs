import random
import string
import networkx as nx
import matplotlib.pyplot as plt

# Fonction pour générer un graphe avec des poids aléatoires
def generate_graph(num_vertices):
    # Générer les étiquettes des sommets (A, B, ..., Z, AA, AB, etc.)
    def generate_labels(n):
        labels = []
        alphabet = string.ascii_uppercase
        for i in range(n):
            label = ""
            temp = i
            while temp >= 0:
                label = alphabet[temp % 26] + label
                temp = temp // 26 - 1
            labels.append(label)
        return labels

    labels = generate_labels(num_vertices)
    
    # Créer un graphe complet avec des poids aléatoires
    G = nx.Graph()
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            weight = random.randint(1, 100)
            G.add_edge(labels[i], labels[j], weight=weight)
    
    return G

# Fonction pour appliquer l'algorithme de Kruskal
def apply_kruskal(G):
    # Applique Kruskal pour obtenir l'arbre couvrant minimal
    mst = nx.minimum_spanning_edges(G, algorithm="kruskal", data=True)
    mst_edges = list(mst)
    total_cost = sum([data['weight'] for u, v, data in mst_edges])
    return mst_edges, total_cost

# Fonction pour visualiser le graphe et l'arbre couvrant minimal (MST)
def visualize_graph(G, mst_edges):
    pos = nx.spring_layout(G)  # Disposition des sommets
    
    # Dessiner tous les sommets et arêtes
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray')
    
    # Dessiner les poids des arêtes
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Mettre en surbrillance les arêtes du MST
    mst_edges_list = [(u, v) for u, v, data in mst_edges]
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges_list, edge_color='green', width=2)
    
    # Afficher le graphe
    plt.title("Visualisation du graphe avec MST en vert")
    plt.show()

# Fonction principale qui inclut tous les processus
def kruskal_mst(num_vertices):
    # Générer le graphe
    G = generate_graph(num_vertices)
    
    # Appliquer l'algorithme de Kruskal
    mst_edges, total_cost = apply_kruskal(G)
    
    # Afficher l'arbre couvrant minimal et son coût
    print("\nArbre couvrant minimal (MST) :")
    for u, v, data in mst_edges:
        print(f"Arête: {u} - {v}, Poids: {data['weight']}")
    print(f"Coût total de l'arbre couvrant minimal: {total_cost}")
    
    # Visualiser le graphe et le MST
    visualize_graph(G, mst_edges)