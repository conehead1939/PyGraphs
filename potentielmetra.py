def run_metra_potential(num_tasks):
    """
    Run the Metra Potential Method for a specified number of tasks.
    Returns the early start dates, late start dates, total duration, and critical path.
    """
    import random

    def generate_task_table(num_tasks):
        """Générer un tableau de tâches avec durées et antériorités."""
        tasks = {}
        for i in range(1, num_tasks + 1):
            duration = random.randint(1, 10)  # Durée aléatoire (1-10 jours)
            predecessors = random.sample(range(1, i), random.randint(0, min(2, i - 1)))
            tasks[f"T{i}"] = {"duration": duration, "predecessors": [f"T{p}" for p in predecessors]}
        return tasks

    def calculate_potential_metra(tasks):
        """Calculer les dates au plus tôt, au plus tard, la durée totale et le chemin critique."""
        early_start = {}
        late_start = {}

        # Calcul des dates au plus tôt
        for task in tasks:
            predecessors = tasks[task]["predecessors"]
            early_start[task] = max([early_start[p] + tasks[p]["duration"] for p in predecessors] + [0])

        # Durée totale du projet
        total_duration = max(early_start[task] + tasks[task]["duration"] for task in tasks)

        # Calcul des dates au plus tard
        late_start = {task: total_duration - tasks[task]["duration"] for task in tasks}
        for task in sorted(tasks, key=lambda x: -early_start[x]):
            successors = [t for t in tasks if task in tasks[t]["predecessors"]]
            if successors:
                late_start[task] = min([late_start[s] - tasks[task]["duration"] for s in successors])

        # Chemin critique
        critical_path = [task for task in tasks if early_start[task] == late_start[task]]

        return early_start, late_start, total_duration, critical_path

    # Generate tasks
    tasks = generate_task_table(num_tasks)

    # Calculate Metra Potential
    early_start, late_start, total_duration, critical_path = calculate_potential_metra(tasks)

    return tasks, early_start, late_start, total_duration, critical_path
