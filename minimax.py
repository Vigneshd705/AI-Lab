import math

def minimax(current_depth, node_index, is_max_turn, leaf_values, total_depth):
    if current_depth == total_depth:
        return leaf_values[node_index]
    
    left_value = minimax(current_depth + 1, node_index * 2, not is_max_turn, leaf_values, total_depth)
    right_value = minimax(current_depth + 1, node_index * 2 + 1, not is_max_turn, leaf_values, total_depth)

    if left_value is None:
        return right_value
    if right_value is None:
        return left_value
    
    return max(left_value, right_value) if is_max_turn else min(left_value, right_value)

leaf_values = list(map(int, input("Enter leaf node values: ").split()))

number_of_leaves = len(leaf_values)
next_power_of_2 = 2 ** math.ceil(math.log2(number_of_leaves))
leaf_values.extend([None] * (next_power_of_2 - number_of_leaves))

total_depth = math.ceil(math.log2(len(leaf_values)))

current_depth = 0
root_node_index = 0
is_max_turn = True

optimal_value = minimax(current_depth, root_node_index, is_max_turn, leaf_values, total_depth)

print("Processed Leaf Nodes:", leaf_values)
print("Total Depth of Tree:", total_depth)
print("Optimal Value:", optimal_value)
