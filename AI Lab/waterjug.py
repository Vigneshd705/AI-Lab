from collections import deque

def print_board(a, b):
    """
    Prints the current state of the jugs.
    """
    print(f"Jug A: {a} liters | Jug B: {b} liters")

def is_goal(a, b, target):
    """
    Checks if either jug has the target volume.
    """
    return a == target or b == target

def get_next_states(a, b, capacity_a, capacity_b):
    """
    Generates all possible next states from the current state.
    """
    states = []
    
    # 1. Fill Jug A
    states.append((capacity_a, b))
    
    # 2. Fill Jug B
    states.append((a, capacity_b))
    
    # 3. Empty Jug A
    states.append((0, b))
    
    # 4. Empty Jug B
    states.append((a, 0))
    
    # 5. Pour Jug A -> Jug B
    pour_to_b = min(a, capacity_b - b)
    new_a = a - pour_to_b
    new_b = b + pour_to_b
    states.append((new_a, new_b))
    
    # 6. Pour Jug B -> Jug A
    pour_to_a = min(b, capacity_a - a)
    new_a = a + pour_to_a
    new_b = b - pour_to_a
    states.append((new_a, new_b))
    
    return states

def water_jug_bfs(capacity_a, capacity_b, target):
    """
    Solves the Water Jug Problem using BFS and returns the path to the target.
    """
    # Initial state: both jugs are empty
    initial_state = (0, 0)
    
    # Queue for BFS: each element is (current_state, path_taken)
    queue = deque()
    queue.append((initial_state, [initial_state]))
    
    # Set to keep track of visited states
    visited = set()
    visited.add(initial_state)
    
    while queue:
        current_state, path = queue.popleft()
        a, b = current_state
        
        # Check if we've reached the target
        if is_goal(a, b, target):
            return path
        
        # Generate all possible next states
        for state in get_next_states(a, b, capacity_a, capacity_b):
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))
    
    # If we've exhausted all possibilities without finding the target
    return None

def main():
    """
    Main function to execute the Water Jug Problem solver.
    """
    print("Water Jug Problem Solver")
    try:
        capacity_a = int(input("Enter the capacity of Jug A (in liters): "))
        capacity_b = int(input("Enter the capacity of Jug B (in liters): "))
        target = int(input("Enter the target volume to measure (in liters): "))
    except ValueError:
        print("Please enter valid integer values for capacities and target.")
        return
    
    # Quick checks to see if the target is achievable
    from math import gcd
    if target > max(capacity_a, capacity_b):
        print("Target volume is greater than both jug capacities. No solution exists.")
        return
    if target % gcd(capacity_a, capacity_b) != 0:
        print(f"No solution exists since {target} is not a multiple of the GCD of {capacity_a} and {capacity_b}.")
        return
    
    path = water_jug_bfs(capacity_a, capacity_b, target)
    
    if path:
        print("\nSteps to reach the target:")
        for step, state in enumerate(path):
            a, b = state
            print(f"Step {step}: ", end="")
            print_board(a, b)
    else:
        print("No solution exists with the given jug capacities and target.")

if __name__ == "__main__":
    main()
