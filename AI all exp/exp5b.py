class TreeNode:
    def __init__(self, label=None):
        self.label = label
        self.children = []

def build_tree_from_input():
    print("Enter the tree nodes in a parent-children format (use '.' for no children):")
    root_label = input("Enter label for root node: ")
    root = TreeNode(root_label)
    queue = [root]
    
    while queue:
        current_node = queue.pop(0)
        
        children_input = input(f"Enter children for {current_node.label} (comma-separated labels or '.' if no children): ").strip()
        
        if children_input == '.':
            continue
        
        child_labels = list(map(str.strip, children_input.split(',')))
        for label in child_labels:
            if label == '.':
                continue
            new_child = TreeNode(label)
            current_node.children.append(new_child)
            queue.append(new_child)
    
    return root

def minimax_ab(node, maximizingPlayer, alpha, beta):
    if not node.children:
        return int(node.label) 
    
    if maximizingPlayer:
        best = float('-inf')
        for child in node.children:
            val = minimax_ab(child, False, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for child in node.children:
            val = minimax_ab(child, True, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

root = build_tree_from_input()
if root is None:
    print("Empty tree!")
else:
    optimalValue = minimax_ab(root, True, float('-inf'), float('inf'))
    print("The optimal value is:", optimalValue)
