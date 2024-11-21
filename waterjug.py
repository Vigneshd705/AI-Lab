def dfs(current_state, target, visited, solution, capacities):
    jug1, jug2 = current_state


    if jug1 == target or jug2 == target:
        solution.append((jug1, jug2))
        print("Solution found:", solution)
        return True

    visited.add(current_state)
    solution.append(current_state)
    
    cap1, cap2 = capacities

    next_states = [
        (cap1, jug2), 
        (jug1, cap2), 
        (0, jug2),     
        (jug1, 0),     
        (max(jug1 - (cap2 - jug2), 0), min(cap2, jug1 + jug2)),
        (min(cap1, jug1 + jug2), max(jug2 - (cap1 - jug1), 0))
    ]

    for next_state in next_states:
        if next_state not in visited:
            if dfs(next_state, target, visited, solution, capacities):
                return True

    solution.pop()
    return False



jug1_capacity = 4
jug2_capacity = 3
target = 2

visited = set()
solution = []

initial_state = (0, 0)
if not dfs(initial_state, target, visited, solution, (jug1_capacity, jug2_capacity)):
    print("No solution found.")

