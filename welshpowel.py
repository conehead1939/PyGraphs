import networkx as nx
import matplotlib.pyplot as plt
import random 
import time

def welshpowel(x):
    def generate_random_graph(x): 
        G = nx.Graph() 
        G.add_nodes_from(range(x)) 
        for i in range(x): 
            for j in range(i + 1, x): 
                if random.choice([True, False]): 
                    G.add_edge(i, j) 
        return G 
 
    plt.show()
    def welch_powell(G):
        # Trier les sommets par ordre décroissant de degrés 
        sommets_tries = sorted(G.nodes(), key=lambda x: G.degree(x), reverse=True) 
        couleur_sommets = {} 
        couleur_actuelle = 0 
        for sommet in sommets_tries:
            # Vérifier les couleurs des voisins
            couleurs_interdites = {couleur_sommets[voisin] 
                                for voisin in G.neighbors(sommet) 
                                if voisin in couleur_sommets} 
            # Trouver une couleur disponible 
            for couleur in range(len(G.nodes())): 
                if couleur not in couleurs_interdites:
                    couleur_sommets[sommet] = couleur 
                    break 
        return couleur_sommets
    def generate_random_colors(n): 
        colors = [] 
        for i in range(n): 
            colors.append('#{:06x}'.format(random.randint(0, 0xFFFFFF))) 
        return colors
    def appliquer_couleurs(G, coloration): 
        n = max(coloration.values()) + 1 
        # Nombre de couleurs utilisées 
        couleurs_aleatoires = generate_random_colors(n) 
        couleurs_sommets = [couleurs_aleatoires[coloration[sommet]] 
                            for sommet in G.nodes()] 
        nx.draw(G, with_labels=True, node_color=couleurs_sommets) 
        plt.show()

    def nombre_chromatique(coloration): 
        return max(coloration.values())+1

    def tic_toc():
        start_time = time.time()
        
        # Generate random graph
        random_graph = generate_random_graph(x)
        
        # Apply Welch-Powell coloring
        coloration = welch_powell(random_graph)
        
        # Apply and display colors
        appliquer_couleurs(random_graph, coloration)
        
        # Calculate chromatic number
        chromatic_number = nombre_chromatique(coloration)
        
        end_time = time.time()
        
        print(f"Le nombre chromatique du graphe est: {chromatic_number}")
        print(f"Le temps d'exécution est de: {end_time - start_time:.4f} secondes")
        
    # Call the function to measure execution time
    tic_toc()
