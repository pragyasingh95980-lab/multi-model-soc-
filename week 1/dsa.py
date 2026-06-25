def compute_max_density(values, span):
    if len(values) < span:
        return 0
    
    running_total = sum(values[:span])
    peak_total = running_total
    
    for i in range(len(values) - span):
        running_total = running_total - values[i] + values[i + span]
        if running_total > peak_total:
            peak_total = running_total
            
    return peak_total

def search_complementary_values(nodes, target_sum):
    low_idx = 0
    high_idx = len(nodes) - 1
    
    while low_idx < high_idx:
        current_eval = nodes[low_idx] + nodes[high_idx]
        if current_eval == target_sum:
            return True
        elif current_eval < target_sum:
            low_idx = low_idx + 1
        else:
            high_idx = high_idx - 1
            
    return False

density_logs = [10, 4, 1, 8, 12, 3, 6, 2]
print(compute_max_density(density_logs, 4))

coordinate_nodes =
print(search_complementary_values(coordinate_nodes, 25))
