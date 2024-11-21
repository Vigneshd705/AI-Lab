import heapq as hq

def ucs(graph, start, goal):
    queue = []
    visited = set()
    hq.heappush(queue, (0, start))  

    while queue:
        cost, curr = hq.heappop(queue) 

        if curr in visited:
            continue

        visited.add(curr)

        print(f"Visiting node: {curr} with cost: {cost}")

        if curr == goal:
            print(f"Goal reached with total cost: {cost}")
            return cost

        for neighbor, step_cost in graph[curr].items():
            if neighbor not in visited:
                hq.heappush(queue, (cost + step_cost, neighbor))

    print("Goal not reachable")
    return float('inf') 

graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'C': 3},
    'C': {'D': 3, 'G': 5},
    'D': {'G': 0},
    'G': {}
}
start = 'A'
goal = 'G'

# Run UCS
ucs(graph, start, goal)
