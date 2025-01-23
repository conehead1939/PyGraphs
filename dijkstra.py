import networkx as nx
import matplotlib.pyplot as plt
import random

def shortest_path_dijkstra(n_sommets, depart, arrivee):
    def generer_graphe_aleatoire(n_sommets):
        graphe = nx.Graph()
        for i in range(n_sommets):
            graphe.add_node(f"X{i}")
        
        # Increase the probability to make the graph less sparse
        for i in range(n_sommets):
            for j in range(i + 1, n_sommets):
                if random.random() < 0.6:  # 60% chance to create a connection
                    poids = random.randint(1, 100)
                    graphe.add_edge(f"X{i}", f"X{j}", weight=poids)

        # Ensure the graph is connected by checking for disconnected components
        if nx.is_connected(graphe):
            return graphe
        else:
            # If disconnected, connect the graph by adding edges between components
            composants = list(nx.connected_components(graphe))
            while len(composants) > 1:
                c1 = composants.pop()
                c2 = composants.pop()
                # Add a random edge between the two components
                node1 = random.choice(list(c1))
                node2 = random.choice(list(c2))
                poids = random.randint(1, 100)
                graphe.add_edge(node1, node2, weight=poids)
                composants = list(nx.connected_components(graphe))  # Recompute components
            return graphe

    def afficher_graphe(graphe, chemin=[], distance=None):
        pos = nx.spring_layout(graphe)  # Layout for visualization

        # Set colors: red for shortest path edges, blue for others
        couleurs = [
            'red' if (chemin and ((u, v) in chemin or (v, u) in chemin)) else 'blue'
            for u, v in graphe.edges()
        ]

        nx.draw(graphe, pos, with_labels=True, node_color='lightgreen', edge_color=couleurs, width=2)

        # Add edge weights
        poids = nx.get_edge_attributes(graphe, 'weight')
        nx.draw_networkx_edge_labels(graphe, pos, edge_labels=poids)

        # Display the shortest path and distance on the graph
        if distance is not None and chemin:
            path_text = f"Shortest Path: {' -> '.join([u for u, _ in chemin] + [chemin[-1][1]])}\nDistance: {distance}"
            plt.text(0.5, 1.05, path_text, horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=10, color='black')

        # Show the total distance on the graph
        if distance is not None:
            total_distance_text = f"Total Distance: {distance}"
            plt.text(0.5, 1.1, total_distance_text, horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12, color='black')

        plt.show()

    def dijkstra(graphe, depart, arrivee):
        try:
            distance, chemin = nx.single_source_dijkstra(graphe, depart, target=arrivee, weight='weight')
            chemin_edges = [(chemin[i], chemin[i + 1]) for i in range(len(chemin) - 1)]
            return distance, chemin_edges
        except nx.NetworkXNoPath:
            print(f"Aucun chemin trouvé entre {depart} et {arrivee}.")
            return None, []

    # Generate the graph with reduced connections
    graphe = generer_graphe_aleatoire(n_sommets)

    # Apply Dijkstra's algorithm
    distance, chemin = dijkstra(graphe, depart, arrivee)

    # Display the graph with the shortest path highlighted
    afficher_graphe(graphe, chemin, distance)