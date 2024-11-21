
def hill_climbing(curr,goal,graph,heuristic,path=None):
    if path==None:
        path=[]
    path.append(curr)
    if curr==goal:
        print("Path found!")
        print(path)
        return True
    neighbors = sorted(graph[curr], key=heuristic.get)
   
    for neighbor in neighbors:
        if neighbor not in path and heuristic[curr]<=heuristic[neighbor]:
            if hill_climbing(neighbor,goal,graph,heuristic,path):
                return True
    return False
    
graph={
    'A':{'B','C'},
    'B':{'C','D'},
    'C':{'E'},
    'D':{'G','E'},
    'E':{'G'},
    'G':{}
}
heuristic={'A':10,'B':11,'C':10,'D':15,'G':30,'E':25}
start='A'
goal='G'
if not hill_climbing(start,goal,graph,heuristic):
    print("Path not found!")