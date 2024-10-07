import random

def objective_function(x):
    """The objective function we want to maximize."""
    return -1 * (x ** 2 - 10 * x)

def get_neighbors(x):
    """Generate neighboring solutions."""
    step_size = 0.1  # Define the step size
    return [x - step_size, x + step_size]

def hill_climbing(initial_solution, max_iterations=100):
    """Hill Climbing algorithm."""
    current_solution = initial_solution
    current_value = objective_function(current_solution)
    
    for _ in range(max_iterations):
        neighbors = get_neighbors(current_solution)
        best_neighbor = None
        best_value = current_value
        
        for neighbor in neighbors:
            neighbor_value = objective_function(neighbor)
            if neighbor_value > best_value:
                best_value = neighbor_value
                best_neighbor = neighbor
        
        if best_neighbor is not None:
            current_solution = best_neighbor
            current_value = best_value
        else:
            break  # Stop if no better neighbor is found
            
    return current_solution, current_value

def main():
    # Randomly initialize the starting point
    initial_solution = random.uniform(0, 10)  # Adjust the range as needed
    print(f"Initial solution: {initial_solution}")
    
    best_solution, best_value = hill_climbing(initial_solution)
    print(f"Best solution found: {best_solution}")
    print(f"Value of the objective function: {best_value}")

if __name__ == "__main__":
    main()
