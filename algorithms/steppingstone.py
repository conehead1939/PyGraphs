import numpy as np 
def run_stepping_stone(costs, allocation):
    """
    Executes the Stepping Stone algorithm on a given cost matrix and initial allocation.
    
    Parameters:
    - costs: 2D numpy array of transportation costs.
    - allocation: 2D numpy array representing the initial feasible allocation.
    
    Returns:
    - final_allocation: 2D numpy array of the final allocation after optimization.
    - total_cost: The total transportation cost for the optimized allocation.
    """
    def stepping_stone(costs, allocation):
        m, n = costs.shape
        while True:
            potential_matrix = np.full((m, n), np.inf)  # Matrix to store reduced costs
            for i in range(m):
                for j in range(n):
                    if allocation[i, j] == 0:  # Check only for empty cells
                        path = find_closed_path(allocation, (i, j))
                        if path:
                            potential_matrix[i, j] = calculate_reduced_cost(path, costs)

            # Find the minimum reduced cost
            min_cost = np.min(potential_matrix)
            if min_cost >= 0:
                break  # Optimal solution found

            # Get the position of the minimum reduced cost
            i, j = np.unravel_index(np.argmin(potential_matrix), potential_matrix.shape)
            path = find_closed_path(allocation, (i, j))
            update_allocation(allocation, path)

        total_cost = np.sum(allocation * costs)
        return allocation, total_cost

    def find_closed_path(allocation, start):
        visited = set()
        path = []

        def dfs(node, direction, prev_direction):
            if node in visited:
                if node == start:
                    path.append(node)
                    return True
                return False
            visited.add(node)
            path.append(node)
            x, y = node
            for dx, dy, new_direction in [(-1, 0, 'up'), (1, 0, 'down'), (0, -1, 'left'), (0, 1, 'right')]:
                if new_direction != prev_direction and 0 <= x+dx < allocation.shape[0] and 0 <= y+dy < allocation.shape[1]:
                    if allocation[x+dx, y+dy] > 0 or (x+dx, y+dy) == start:
                        if dfs((x+dx, y+dy), new_direction, direction):
                            return True
            path.pop()
            return False

        if dfs(start, None, None):
            return path
        return None

    def calculate_reduced_cost(path, costs):
        cost = 0
        sign = 1
        for (x, y) in path:
            cost += sign * costs[x, y]
            sign *= -1
        return cost

    def update_allocation(allocation, path):
        deltas = [allocation[x, y] for i, (x, y) in enumerate(path) if i % 2 == 1]
        theta = min(deltas)
        sign = 1
        for (x, y) in path:
            allocation[x, y] += sign * theta
            sign *= -1

    # Run the stepping stone algorithm
    final_allocation, total_cost = stepping_stone(costs, allocation)
    return final_allocation, total_cost