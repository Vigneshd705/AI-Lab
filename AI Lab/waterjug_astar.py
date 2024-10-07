
import heapq

class State:
    """Class to represent a state in the Water Jug problem."""
    def __init__(self, jug1, jug2, capacity1, capacity2):
        self.jug1 = jug1  # Current amount of water in jug1
        self.jug2 = jug2  # Current amount of water in jug2
        self.capacity1 = capacity1  # Maximum capacity of jug1
        self.capacity2 = capacity2  # Maximum capacity of jug2

    def is_goal(self, goal):
        """Check if the current state is the goal state."""
        return self.jug1 == goal or self.jug2 == goal

    def heuristic(self, goal):
        """Calculate the heuristic based on the goal."""
        return abs(goal - self.jug1) + abs(goal - self.jug2)

    def get_neighbors(self):
        """Generate all possible states from the current state."""
        neighbors = []

        # Fill jug1
        neighbors.append(State(self.capacity1, self.jug2, self.capacity1, self.capacity2))
        # Fill jug2
        neighbors.append(State(self.jug1, self.capacity2, self.capacity1, self.capacity2))
        # Empty jug1
        neighbors.append(State(0, self.jug2, self.capacity1, self.capacity2))
        # Empty jug2
        neighbors.append(State(self.jug1, 0, self.capacity1, self.capacity2))
        # Pour jug1 into jug2
        pour_amount = min(self.jug1, self.capacity2 - self.jug2)
        neighbors.append(State(self.jug1 - pour_amount, self.jug2 + pour_amount, self.capacity1, self.capacity2))
        # Pour jug2 into jug1
        pour_amount = min(self.jug2, self.capacity1 - self.jug1)
        neighbors.append(State(self.jug1 + pour_amount, self.jug2 - pour_amount, self.capacity1, self.capacity2))

        return neighbors

def a_star_water_jug(capacity1, capacity2, goal):
    """A* algorithm implementation for the Water Jug problem."""
    start_state = State(0, 0, capacity1, capacity2)
    open_list = []
    heapq.heappush(open_list, (0, start_state))  # (cost, state)
    closed_set = set()

    while open_list:
        current_cost, current_state = heapq.heappop(open_list)

        # If the current state is the goal, return success
        if current_state.is_goal(goal):
            return True

        # Mark this state as explored
        closed_set.add((current_state.jug1, current_state.jug2))

        for neighbor in current_state.get_neighbors():
            if (neighbor.jug1, neighbor.jug2) not in closed_set:
                # Calculate cost to reach the neighbor
                cost = current_cost + 1  # Each action has a cost of 1
                heapq.heappush(open_list, (cost + neighbor.heuristic(goal), neighbor))

    return False  # No solution found

def main():
    capacity1 = 4  # Capacity of jug1
    capacity2 = 3  # Capacity of jug2
    goal = 2       # Goal amount of water

    if a_star_water_jug(capacity1, capacity2, goal):
        print("Path to the goal found!")
    else:
        print("No path found!")

if __name__ == "__main__":
    main()
