import numpy as np

def supply_chain_algorithms(nb_usines, nb_magasins, min_cost=1, max_cost=20, min_cap=10, max_cap=50):
    """Wraps the data generation, North-West corner, and Least-Cost algorithms."""
    
    def generate_data(nb_usines, nb_magasins, min_cost, max_cost, min_cap, max_cap):
        """Génère des données aléatoires pour les coûts, capacités et demandes."""
        couts = np.random.randint(min_cost, max_cost, size=(nb_usines, nb_magasins))
        capacites = np.random.randint(min_cap, max_cap, size=nb_usines)
        demandes = np.random.randint(min_cap, max_cap, size=nb_magasins)

        total_capacite = sum(capacites)
        total_demande = sum(demandes)
        if total_capacite > total_demande:
            demandes[-1] += total_capacite - total_demande
        else:
            capacites[-1] += total_demande - total_capacite

        return couts, capacites, demandes

    def calculer_cout_total(couts, allocation):
        """Calcule le coût total pour une allocation donnée."""
        return np.sum(couts * allocation)

    def nord_ouest(capacites, demandes):
        """Applique l'algorithme Nord-Ouest pour une allocation initiale."""
        allocation = np.zeros((len(capacites), len(demandes)), dtype=int)
        i, j = 0, 0
        while i < len(capacites) and j < len(demandes):
            alloc = min(capacites[i], demandes[j])
            allocation[i, j] = alloc
            capacites[i] -= alloc
            demandes[j] -= alloc
            if capacites[i] == 0:
                i += 1
            if demandes[j] == 0:
                j += 1
        return allocation

    def moindre_cout(couts, capacites, demandes):
        """Applique l'algorithme des moindres coûts pour une allocation initiale."""
        allocation = np.zeros_like(couts, dtype=int)
        couts_temp = couts.astype(float)
        while np.any(capacites) and np.any(demandes):
            i, j = np.unravel_index(np.argmin(couts_temp, axis=None), couts_temp.shape)
            alloc = min(capacites[i], demandes[j])
            allocation[i, j] = alloc
            capacites[i] -= alloc
            demandes[j] -= alloc
            if capacites[i] == 0:
                couts_temp[i, :] = np.inf
            if demandes[j] == 0:
                couts_temp[:, j] = np.inf
        return allocation

    # Generate data
    couts, capacites, demandes = generate_data(nb_usines, nb_magasins, min_cost, max_cost, min_cap, max_cap)

    # Apply North-West corner method
    nw_capacites = capacites.copy()
    nw_demandes = demandes.copy()
    allocation_nw = nord_ouest(nw_capacites, nw_demandes)
    total_cost_nw = calculer_cout_total(couts, allocation_nw)

    # Apply Least-Cost method
    lc_capacites = capacites.copy()
    lc_demandes = demandes.copy()
    allocation_lc = moindre_cout(couts, lc_capacites, lc_demandes)
    total_cost_lc = calculer_cout_total(couts, allocation_lc)

    return {
        "cost_matrix": couts,
        "allocation_nw": allocation_nw,
        "total_cost_nw": total_cost_nw,
        "allocation_lc": allocation_lc,
        "total_cost_lc": total_cost_lc
    }