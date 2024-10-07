class Graph:
    def __init__(self):
        self.nodes = {}
        self.heuristic = {}

    def add_edge(self, from_node, to_node, weight=1):
        if from_node not in self.nodes:
            self.nodes[from_node] = {}
        if to_node not in self.nodes:
            self.nodes[to_node] = {}
        self.nodes[from_node][to_node] = weight

    def set_heuristic(self, node, value):
        self.heuristic[node] = value

    def hill_climbing(self, start, goal):
        current_node = start
        path = [start]

        while current_node != goal:
            print(f"Current Node: {current_node}")

            if current_node not in self.nodes or len(self.nodes[current_node]) == 0:
                print("No more nodes to visit. Stuck at a local maximum.")
                return path

            neighbors = self.nodes[current_node]
            next_node = None
            next_heuristic = float('inf')

            for neighbor in neighbors:
                if self.heuristic[neighbor] < next_heuristic:
                    next_node = neighbor
                    next_heuristic = self.heuristic[neighbor]

            if next_heuristic >= self.heuristic[current_node]:
                print("No better neighbors found. Reached a local maximum.")
                return path

            current_node = next_node
            path.append(current_node)

        print(f"Goal Node {goal} reached.")
        return path


# Example usage
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('A', 'D')
    graph.add_edge('C', 'Z')
    graph.add_edge('C', 'E')

    # Set heuristic values for each node
    graph.set_heuristic('A', 5)
    graph.set_heuristic('B', 5)
    graph.set_heuristic('C', 3)
    graph.set_heuristic('D', 4)
    graph.set_heuristic('E', 2)
    graph.set_heuristic('Z', 1)
    

    # Perform hill climbing
    start_node = 'A'
    goal_node = 'Z'
    path = graph.hill_climbing(start_node, goal_node)
    print(f"Path from {start_node} to {goal_node}: {path}")