import heapq
def find_position(state, value):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == value:
                return i, j
def manhattan_distance(state, goal):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0: 
                goal_i, goal_j = find_position(goal, state[i][j])
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def a_star_8_puzzle(start, goal):
    pq = []
    heapq.heappush(pq, (0, 0, start, []))
    visited = set()

    start_tuple = tuple(tuple(row) for row in start)
    goal_tuple = tuple(tuple(row) for row in goal)
    visited.add(start_tuple)

    while pq:
        f_score, g_score, current, path = heapq.heappop(pq)

        if tuple(tuple(row) for row in current) == goal_tuple:
            return g_score, path

        x, y = find_position(current, 0)

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in current]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                new_state_tuple = tuple(tuple(row) for row in new_state)

                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    new_g_score = g_score + 1
                    new_h_score = manhattan_distance(new_state, goal)
                    new_f_score = new_g_score + new_h_score
                    heapq.heappush(pq, (new_f_score, new_g_score, new_state, path + [new_state]))

    return float('inf'), [] 
start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
cost, solution_path = a_star_8_puzzle(start, goal)

print(f"Cost: {cost}")
print("Solution Path:")
for step in solution_path:
    for row in step:
        print(row)
    print()
