import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import numpy as np
import FordFulkerson
from Kruskal import kruskal_mst, visualize_graph
from Nord_ouest import supply_chain_algorithms
import Nord_ouest
from bellmanford import run_bellman_ford
from dijkstra import shortest_path_dijkstra
from FordFulkerson import ford_fulkerson, generer_graphe_oriente_avec_capacites, afficher_graphe
from potentielmetra import run_metra_potential
from steppingstone import run_stepping_stone
import welshpowel
def interface():
    def Welsh_Powel():
        new_window = tk.Toplevel()
        new_window.title("Welsh Powel")
        new_window.geometry("400x200")

        label = tk.Label(new_window, text="Enter number of nodes:")
        label.pack(pady=10)

        entry = tk.Entry(new_window, width=30)
        entry.pack(pady=5)

        submit_button = tk.Button(new_window, text="Submit", command=lambda: welshpowel.welshpowel(int(entry.get())))
        submit_button.pack(pady=10)

    def Dijkstra():
        def run_dijkstra():
            n_sommets = int(entry_n.get())
            depart = entry_start.get()
            arrivee = entry_end.get()
            shortest_path_dijkstra(n_sommets, depart, arrivee)  

        new_window = tk.Toplevel()
        new_window.title("Dijkstra")
        new_window.geometry("400x300")

        label_n = tk.Label(new_window, text="Enter number of nodes:")
        label_n.pack(pady=5)

        entry_n = tk.Entry(new_window, width=30)
        entry_n.pack(pady=5)

        label_start = tk.Label(new_window, text="Enter start node (e.g., X0):")
        label_start.pack(pady=5)

        entry_start = tk.Entry(new_window, width=30)
        entry_start.pack(pady=5)

        label_end = tk.Label(new_window, text="Enter end node (e.g., X1):")
        label_end.pack(pady=5)

        entry_end = tk.Entry(new_window, width=30)
        entry_end.pack(pady=5)

        submit_button = tk.Button(new_window, text="Submit", command=run_dijkstra)
        submit_button.pack(pady=10)

    
    def Potentiel_Metra():
        def run_metra():
            try:
                num_tasks = int(entry.get())
                if num_tasks <= 0:
                    raise ValueError("Number of tasks must be greater than 0.")
                
                # Run the Metra Potential method
                tasks, early_start, late_start, total_duration, critical_path = run_metra_potential(num_tasks)
                
                # Display results in a new window
                results_window = tk.Toplevel()
                results_window.title("Potentiel Metra Results")
                results_window.geometry("800x600")
                
                # Create two columns using frames
                left_frame = tk.Frame(results_window)
                left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
                
                right_frame = tk.Frame(results_window)
                right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
                
                # Left column: Tasks
                tasks_label = tk.Label(left_frame, text="Tasks:", font=("Arial", 14, "bold"))
                tasks_label.pack(pady=5)
                for task, details in tasks.items():
                    task_info = f"{task}: Duration = {details['duration']}, Predecessors = {', '.join(details['predecessors']) or 'None'}"
                    tk.Label(left_frame, text=task_info, font=("Arial", 10)).pack(anchor="w")
                
                # Right column: Results
                early_label = tk.Label(right_frame, text="Early Start Dates:", font=("Arial", 14, "bold"))
                early_label.pack(pady=5)
                for task, date in early_start.items():
                    tk.Label(right_frame, text=f"{task}: {date}", font=("Arial", 10)).pack(anchor="w")
                
                late_label = tk.Label(right_frame, text="\nLate Start Dates:", font=("Arial", 14, "bold"))
                late_label.pack(pady=5)
                for task, date in late_start.items():
                    tk.Label(right_frame, text=f"{task}: {date}", font=("Arial", 10)).pack(anchor="w")
                
                total_duration_label = tk.Label(right_frame, text=f"\nTotal Project Duration: {total_duration} days", font=("Arial", 14, "bold"))
                total_duration_label.pack(pady=10)
                
                critical_path_label = tk.Label(right_frame, text=f"Critical Path: {' -> '.join(critical_path)}", font=("Arial", 14, "bold"))
                critical_path_label.pack(pady=10)
            
            except ValueError as e:
                messagebox.showerror("Invalid Input", f"Error: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")

        # Create the input window
        new_window = tk.Toplevel()
        new_window.title("Potentiel Metra")
        new_window.geometry("400x200")

        label = tk.Label(new_window, text="Enter the number of tasks:", font=("Arial", 12))
        label.pack(pady=10)

        entry = tk.Entry(new_window, width=30)
        entry.pack(pady=5)

        submit_button = tk.Button(new_window, text="Submit", command=run_metra, font=("Arial", 12))
        submit_button.pack(pady=10)

    def Kruskal():
        def on_submit():
            try:
                num_vertices = int(entry.get())
                result, G, mst_edges = kruskal_mst(num_vertices)
                
                
                result_label.config(text=result)
                
                
                visualize_graph(G, mst_edges)
            except ValueError:
                result_label.config(text="Please enter a valid number.")

        new_window = tk.Toplevel()
        new_window.title("Kruskal")
        new_window.geometry("400x300")

        label = tk.Label(new_window, text="Enter the number of vertices:")
        label.pack(pady=10)

        entry = tk.Entry(new_window, width=30)
        entry.pack(pady=5)

        submit_button = tk.Button(new_window, text="Submit", command=on_submit)
        submit_button.pack(pady=10)
        
        result_label = tk.Label(new_window, text="", justify="left")
        result_label.pack(pady=10)

    def Bellman_Ford():
        
        new_window = tk.Toplevel()
        new_window.title("Bellman Ford")
        new_window.geometry("400x400")

        label = tk.Label(new_window, text="Enter the number of vertices:")
        label.pack(pady=10)

        entry_vertices = tk.Entry(new_window, width=30)
        entry_vertices.pack(pady=5)

        label_source = tk.Label(new_window, text="Enter the source node (e.g., x0):")
        label_source.pack(pady=10)

        entry_source = tk.Entry(new_window, width=30)
        entry_source.pack(pady=5)

        label_target = tk.Label(new_window, text="Enter the target node (e.g., x1):")
        label_target.pack(pady=10)

        entry_target = tk.Entry(new_window, width=30)
        entry_target.pack(pady=5)

        result_label = tk.Label(new_window, text="", justify="left", anchor="w")
        result_label.pack(pady=10, padx=10)

        def on_submit():
            try:
                
                num_vertices = int(entry_vertices.get())
                source = entry_source.get().strip().lower()  
                target = entry_target.get().strip().lower()  
                
                
                result = run_bellman_ford(num_vertices, source, target)
                
                
                if result:
                    chemin, distance = result
                    result_text = f"Distance from {source} to {target}: {distance}\nPath: {' -> '.join(chemin)}"
                    result_label.config(text=result_text)
                else:
                    result_label.config(text="No path found.")
            except ValueError:
                result_label.config(text="Please enter valid numbers.")

        
        submit_button = tk.Button(new_window, text="Submit", command=on_submit)
        submit_button.pack(pady=10)

    def Ford_Fulkerson():
        # Create a new window for Ford-Fulkerson inputs
        new_window = tk.Toplevel()
        new_window.title("Ford-Fulkerson")
        new_window.geometry("400x400")

        label = tk.Label(new_window, text="Enter the number of vertices:")
        label.pack(pady=10)

        entry_vertices = tk.Entry(new_window, width=30)
        entry_vertices.pack(pady=5)

        label_source = tk.Label(new_window, text="Enter the source node (e.g., x0):")
        label_source.pack(pady=10)

        entry_source = tk.Entry(new_window, width=30)
        entry_source.pack(pady=5)

        label_target = tk.Label(new_window, text="Enter the target node (e.g., x1):")
        label_target.pack(pady=10)

        entry_target = tk.Entry(new_window, width=30)
        entry_target.pack(pady=5)

        result_label = tk.Label(new_window, text="", justify="left", anchor="w")
        result_label.pack(pady=10, padx=10)

        def on_submit():
            try:
                # Get the input values from the entry fields
                num_vertices = int(entry_vertices.get())
                source = entry_source.get().strip().lower()  # Convert to lowercase to match node labels
                target = entry_target.get().strip().lower()  # Convert to lowercase to match node labels
                
                # Generate the directed graph with capacities
                G = generer_graphe_oriente_avec_capacites(num_vertices)
                
                # Apply the Ford-Fulkerson algorithm
                max_flow = ford_fulkerson(G, source, target)
                
                # Display the result in the new window
                result_label.config(text=f"Max Flow from {source} to {target}: {max_flow}")
                
                # Visualize the graph with flow
                afficher_graphe(G, flow=[(u, v, d['capacity']) for u, v, d in G.edges(data=True)])

            except ValueError:
                result_label.config(text="Please enter valid numbers.")

        # Submit button to trigger the Ford-Fulkerson process
        submit_button = tk.Button(new_window, text="Submit", command=on_submit)
        submit_button.pack(pady=10)

    
    def create_table(window, data, title):
        """Creates a table in the given tkinter window."""
        table_frame = tk.Frame(window)
        table_frame.pack(pady=10, padx=10, fill="both", expand=True)

        tk.Label(table_frame, text=title, font=("Arial", 12, "bold")).pack()

        tree = ttk.Treeview(table_frame, columns=list(range(len(data[0]))), show="headings")
        for i in range(len(data[0])):
            tree.heading(i, text=f"Col {i+1}")
            tree.column(i, width=100, anchor="center")

        for row in data:
            tree.insert("", "end", values=row)

        tree.pack(fill="both", expand=True)

    def Nord_Ouest():
        def calculate_nord_ouest():
            try:
                nb_usines = int(factories_entry.get())
                nb_magasins = int(warehouses_entry.get())

                # Run supply chain algorithms
                result = supply_chain_algorithms(nb_usines, nb_magasins)

                # Create a new results window
                result_window = tk.Toplevel()
                result_window.title("Nord-Ouest Results")
                result_window.geometry("700x500")

                # Display the cost matrix
                create_table(result_window, result["cost_matrix"], "Cost Matrix")

                # Display the allocation
                create_table(result_window, result["allocation_nw"], "Allocation (North-West)")
                print(result["total_cost_nw"])
                # Display the total cost below the tables
                total_cost_text = f"Total Cost (North-West): {result['total_cost_nw']}"
                total_cost_label = tk.Label(
                    result_window, 
                    text=total_cost_text,
                    font=("Arial", 12, "bold"),
                    anchor="center"
                )
                total_cost_label.pack(pady=20)  # Ensure it's displayed with enough spacing

            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid integer values.")

        new_window = tk.Toplevel()
        new_window.title("Nord-Ouest")
        new_window.geometry("400x200")

        tk.Label(new_window, text="Number of Factories:").pack(pady=5)
        factories_entry = tk.Entry(new_window, width=20)
        factories_entry.pack(pady=5)

        tk.Label(new_window, text="Number of Warehouses:").pack(pady=5)
        warehouses_entry = tk.Entry(new_window, width=20)
        warehouses_entry.pack(pady=5)

        submit_button = tk.Button(new_window, text="Submit", command=calculate_nord_ouest)
        submit_button.pack(pady=10)


    def Moindre_Cout():
        def calculate_moindre_cout():
            try:
                nb_usines = int(factories_entry.get())
                nb_magasins = int(warehouses_entry.get())

                # Run supply chain algorithms
                result = supply_chain_algorithms(nb_usines, nb_magasins)

                # Create a new results window
                result_window = tk.Toplevel()
                result_window.title("Moindre Cout Results")
                result_window.geometry("700x500")

                # Display the cost matrix
                create_table(result_window, result["cost_matrix"], "Cost Matrix")

                # Display the allocation
                create_table(result_window, result["allocation_lc"], "Allocation (Least-Cost)")

                # Display the total cost below the tables
                total_cost_text = f"Total Cost (Least-Cost): {result['total_cost_lc']}"
                total_cost_label = tk.Label(
                    result_window, 
                    text=total_cost_text,
                    font=("Arial", 12, "bold"),
                    anchor="center"
                )
                total_cost_label.pack(pady=20)  # Ensure it's displayed with enough spacing

            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid integer values.")

        new_window = tk.Toplevel()
        new_window.title("Moindre Cout")
        new_window.geometry("400x200")

        tk.Label(new_window, text="Number of Factories:").pack(pady=5)
        factories_entry = tk.Entry(new_window, width=20)
        factories_entry.pack(pady=5)

        tk.Label(new_window, text="Number of Warehouses:").pack(pady=5)
        warehouses_entry = tk.Entry(new_window, width=20)
        warehouses_entry.pack(pady=5)

        submit_button = tk.Button(new_window, text="Submit", command=calculate_moindre_cout)
        submit_button.pack(pady=10)

    def Stepping_Stone():
        def calculate_and_display():
            try:
                # Get the number of factories and warehouses
                nb_factories = int(factories_entry.get())
                nb_warehouses = int(warehouses_entry.get())

                # Run the supply chain algorithms
                results = supply_chain_algorithms(nb_factories, nb_warehouses)

                # Extract results
                cost_matrix = results["cost_matrix"]
                allocation_nw = results["allocation_nw"]
                total_cost_nw = results["total_cost_nw"]
                allocation_lc = results["allocation_lc"]
                total_cost_lc = results["total_cost_lc"]

                # Determine the better initial allocation
                if total_cost_nw < total_cost_lc:
                    initial_allocation = allocation_nw
                    initial_total_cost = total_cost_nw
                else:
                    initial_allocation = allocation_lc
                    initial_total_cost = total_cost_lc

                # Run Stepping Stone
                final_allocation, total_cost = run_stepping_stone(cost_matrix, initial_allocation)

                # Display results in a new window
                result_window = tk.Toplevel(new_window)
                result_window.title("Stepping Stone Results")
                result_window.geometry("600x500")

                ttk.Label(result_window, text="Cost Matrix:", font=("Arial", 14)).pack(pady=10)
                cost_table = ttk.Treeview(result_window, columns=list(range(cost_matrix.shape[1])), show='headings', height=cost_matrix.shape[0])
                for i in range(cost_matrix.shape[1]):
                    cost_table.heading(i, text=f"Column {i+1}")
                for row in cost_matrix:
                    cost_table.insert("", tk.END, values=row)
                cost_table.pack(pady=10)

                ttk.Label(result_window, text="Final Allocation:", font=("Arial", 14)).pack(pady=10)
                allocation_table = ttk.Treeview(result_window, columns=list(range(final_allocation.shape[1])), show='headings', height=final_allocation.shape[0])
                for i in range(final_allocation.shape[1]):
                    allocation_table.heading(i, text=f"Column {i+1}")
                for row in final_allocation:
                    allocation_table.insert("", tk.END, values=row)
                allocation_table.pack(pady=10)

                ttk.Label(result_window, text=f"Initial Total Cost: {initial_total_cost}", font=("Arial", 12)).pack(pady=10)
                ttk.Label(result_window, text=f"Optimized Total Cost: {total_cost}", font=("Arial", 14)).pack(pady=10)

            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")

        new_window = tk.Toplevel()
        new_window.title("Stepping Stone")
        new_window.geometry("500x300")

        ttk.Label(new_window, text="Enter Number of Factories:", font=("Arial", 12)).pack(pady=10)
        factories_entry = tk.Entry(new_window, width=30)
        factories_entry.pack(pady=5)

        ttk.Label(new_window, text="Enter Number of Warehouses:", font=("Arial", 12)).pack(pady=10)
        warehouses_entry = tk.Entry(new_window, width=30)
        warehouses_entry.pack(pady=5)

        submit_button = tk.Button(new_window, text="Submit", width=15, command=calculate_and_display)
        submit_button.pack(pady=20)


    root = tk.Tk()
    root.title("Graph Algorithms")

    # Set window dimensions
    root.geometry("600x400")

    # Create a canvas to hold the buttons
    canvas = tk.Canvas(root, bg="white", bd=2, relief="ridge")
    canvas.pack(fill="both", expand=True, padx=10, pady=10)

    # Add buttons (representing the rectangles in the image)
    buttons = [
        ("Welsh Powel", 200, 50, Welsh_Powel),
        ("Dijkstra", 300, 50, Dijkstra),
        ("Potentiel Metra", 400, 50, Potentiel_Metra),
        ("Kruskal", 200, 150, Kruskal),
        ("Bellman Ford", 300, 150, Bellman_Ford),
        ("Ford Fulckerson", 400, 150, Ford_Fulkerson),
        ("Nord-Ouest", 200, 250, Nord_Ouest),
        ("Moindre Cout", 300, 250, Moindre_Cout),
        ("Steeping-Stone", 400, 250, Stepping_Stone),
    ]

    # Create button widgets on the canvas
    for text, x, y, command in buttons:
        button = tk.Button(canvas, text=text, width=15, height=2, relief="groove", command=command)
        canvas.create_window(x, y, window=button)

    # Run the application
    root.mainloop()
