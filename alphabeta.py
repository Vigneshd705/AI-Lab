import math

def minimax_with_alpha_beta(current_depth, node_index, is_maximizing_player, leaf_values, total_depth, alpha, beta, depth=0):
    if current_depth == total_depth:
        return leaf_values[node_index]
    
    indent = "  " * depth  

    if is_maximizing_player:
        max_value = float('-inf')
        left_value = minimax_with_alpha_beta(current_depth + 1, node_index * 2, False, leaf_values, total_depth, alpha, beta, depth + 1)
        max_value = max(max_value, left_value)
        alpha = max(alpha, left_value)
        if beta <= alpha:
            print(f"{indent}Pruning at right child of node {node_index} (maximizing, depth {current_depth + 1})")
            return max_value

        right_value = minimax_with_alpha_beta(current_depth + 1, node_index * 2 + 1, False, leaf_values, total_depth, alpha, beta, depth + 1)
        max_value = max(max_value, right_value)
        alpha = max(alpha, right_value)
        if beta <= alpha:
            print(f"{indent}Pruning at right child of node {node_index} (maximizing, depth {current_depth + 1})")
            return max_value

        return max_value

    else:  
        min_value = float('inf')
        left_value = minimax_with_alpha_beta(current_depth + 1, node_index * 2, True, leaf_values, total_depth, alpha, beta, depth + 1)
        min_value = min(min_value, left_value)
        beta = min(beta, left_value)
        if beta <= alpha:
            print(f"{indent}Pruning at right child of node {node_index} (minimizing, depth {current_depth + 1})")
            return min_value

        right_value = minimax_with_alpha_beta(current_depth + 1, node_index * 2 + 1, True, leaf_values, total_depth, alpha, beta, depth + 1)
        min_value = min(min_value, right_value)
        beta = min(beta, right_value)
        if beta <= alpha:
            print(f"{indent}Pruning at right child of node {node_index} (minimizing, depth {current_depth + 1})")
            return min_value

        return min_value


leaf_values = list(map(int, input("Enter leaf node values: ").split()))

total_depth = math.ceil(math.log2(len(leaf_values)))

current_depth = 0
root_node_index = 0
is_maximizing_player = True
alpha = float('-inf')
beta = float('inf')

optimal_value = minimax_with_alpha_beta(
    current_depth, root_node_index, is_maximizing_player, leaf_values, total_depth, alpha, beta
)

print("Optimal Value:", optimal_value)
