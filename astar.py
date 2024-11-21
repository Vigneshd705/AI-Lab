import heapq as hq

def a_star_algorithm(start_node, goal_node, graph):
    open_set = []
    hq.heappush(open_set, (0, start_node))
    
    cost_to_reach = {}
    for node in graph:
        cost_to_reach[node] = float('inf')
    cost_to_reach[start_node] = 0
    
    parent_node = {}
    
    while open_set:
        _, current_node = hq.heappop(open_set)
        
        if current_node == goal_node:
            path = []
            while current_node in parent_node:
                path.append(current_node)
                current_node = parent_node[current_node]
            path.append(start_node)
            return path[::-1], cost_to_reach[goal_node]
        
        for neighbor, edge_cost in graph[current_node].items():
            tentative_cost = cost_to_reach[current_node] + edge_cost
            if tentative_cost < cost_to_reach[neighbor]:
                cost_to_reach[neighbor] = tentative_cost
                parent_node[neighbor] = current_node
                hq.heappush(open_set, (tentative_cost + heuristic[neighbor], neighbor))
    
    return None, float('inf')

graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 5},
    'C': {'D': 3, 'G': 4},
    'D': {'G': 0},
    'G': {},
    'S': {'A': 1, 'G': 10}
}

heuristic = {
    'A': 3, 'B': 4, 'C': 2,
    'D': 6, 'G': 0, 'S': 5
}

start_node = 'S'
goal_node = 'G'

print(a_star_algorithm(start_node, goal_node, graph))
