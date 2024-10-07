from collections import deque

def water_jug(m, n, start, goal):
    
    visited = set()
    
    queue = deque([(start[0], start[1], [])])

    while queue:
        jug1, jug2, path = queue.popleft()

       
        if (jug1, jug2) == goal:
            return path + [(jug1, jug2)]

       
        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        
        possible_states = [
            (m, jug2),  # Fill Jug 1
            (jug1, n),  # Fill Jug 2
            (0, jug2),  # Empty Jug 1
            (jug1, 0),  # Empty Jug 2
            (jug1 - min(jug1, n - jug2), jug2 + min(jug1, n - jug2)),  # Pour Jug 1 -> Jug 2
            (jug1 + min(jug2, m - jug1), jug2 - min(jug2, m - jug1))   # Pour Jug 2 -> Jug 1
        ]

        for state in possible_states:
            if state not in visited:
                queue.append((*state, path + [(jug1, jug2)]))

    return None 

def main():
    m = int(input("Enter the capacity of Jug 1: "))
    n = int(input("Enter the capacity of Jug 2: "))
    
    print("Enter the initial state:")
    start_jug1 = int(input("Enter the amount of water in Jug 1: "))
    start_jug2 = int(input("Enter the amount of water in Jug 2: "))
    start = (start_jug1, start_jug2)
    
    print("Enter the goal state:")
    goal_jug1 = int(input("Enter the desired amount of water in Jug 1: "))
    goal_jug2 = int(input("Enter the desired amount of water in Jug 2: "))
    goal = (goal_jug1, goal_jug2)

    result = water_jug(m, n, start, goal)
    if result:
        print("Path to reach the goal state:")
        for step in result:
            print(step)
    else:
        print("No solution found")
main()