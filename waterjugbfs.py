from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    # Initialize the queue for BFS
    queue = deque()
    queue.append((0, 0))  # Start with both jugs empty

    # Track visited states to avoid revisiting them
    visited = set()
    visited.add((0, 0))

    # Store the solution path
    parent = {}

    # BFS loop
    while queue:
        current_state = queue.popleft()
        jug1, jug2 = current_state

        # Check if we've reached the target
        if jug1 == target or jug2 == target:
            print_solution_path(current_state, parent)
            return

        # Generate all possible next states
        next_states = generate_next_states(jug1, jug2, jug1_capacity, jug2_capacity)

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
                parent[state] = current_state

    # If the queue is empty and no solution was found
    print("No solution found.")

def generate_next_states(jug1, jug2, cap1, cap2):
    # List of all possible moves
    return [
        (cap1, jug2),  # Fill Jug 1
        (jug1, cap2),  # Fill Jug 2
        (0, jug2),     # Empty Jug 1
        (jug1, 0),     # Empty Jug 2
        # Pour from Jug 1 to Jug 2
        (max(jug1 - (cap2 - jug2), 0), min(cap2, jug1 + jug2)),
        # Pour from Jug 2 to Jug 1
        (min(cap1, jug1 + jug2), max(jug2 - (cap1 - jug1), 0))
    ]

def print_solution_path(state, parent):
    # Reconstruct the path from the parent dictionary
    path = []
    while state:
        path.append(state)
        state = parent.get(state)

    # Print the path in reverse (from start to end)
    path.reverse()
    print("Solution found:")
    for step in path:
        print(step)

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2

water_jug_bfs(jug1_capacity, jug2_capacity, target)
