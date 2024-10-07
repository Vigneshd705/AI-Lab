import heapq

class PuzzleState:
    """Class to represent the state of the 8-Puzzle."""
    def __init__(self, board, zero_pos, moves=0):
        self.board = board  # Current board configuration
        self.zero_pos = zero_pos  # Position of the zero tile
        self.moves = moves  # Number of moves made

    def is_goal(self):
        """Check if the current state is the goal state."""
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def heuristic(self):
        """Calculate the Manhattan distance heuristic."""
        distance = 0
        for index, value in enumerate(self.board):
            if value != 0:  # Ignore the empty tile
                target_x = (value - 1) // 3
                target_y = (value - 1) % 3
                current_x = index // 3
                current_y = index % 3
                distance += abs(target_x - current_x) + abs(target_y - current_y)
        return distance

    def get_neighbors(self):
        """Generate all possible moves from the current state."""
        neighbors = []
        x, y = self.zero_pos

        # Possible moves (up, down, left, right)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:  # Ensure within bounds
                new_board = self.board[:]
                # Swap the zero tile with the adjacent tile
                new_board[x * 3 + y], new_board[new_x * 3 + new_y] = new_board[new_x * 3 + new_y], new_board[x * 3 + y]
                neighbors.append(PuzzleState(new_board, (new_x, new_y), self.moves + 1))

        return neighbors

def greedy_best_first_search(initial_state):
    """Greedy Best-First Search algorithm for solving the 8-Puzzle."""
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, (initial_state.heuristic(), initial_state))

    while open_list:
        _, current_state = heapq.heappop(open_list)

        # Check if the current state is the goal state
        if current_state.is_goal():
            print(f"Goal reached in {current_state.moves} moves!")
            return

        closed_set.add(tuple(current_state.board))  # Add to closed set

        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.board) not in closed_set:  # Check if the neighbor has been explored
                heapq.heappush(open_list, (neighbor.heuristic(), neighbor))

    print("No solution found!")

def main():
    # Initial board configuration (0 represents the empty tile)
    initial_board = [1, 2, 3, 4, 0, 5, 6, 7, 8]  # Change this to test other configurations
    zero_position = (1, 1)  # Position of the empty tile (0)
    initial_state = PuzzleState(initial_board, zero_position)

    greedy_best_first_search(initial_state)

if __name__ == "__main__":
    main()
