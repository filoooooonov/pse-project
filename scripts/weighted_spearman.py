import numpy as np
from scipy import stats

def weighted_spearman(x, y, weights):

    '''
    Computes Spearman's correlation with weighted observations
    
    Note: For weighted correlation, exact p-value calculation is complex,
    the p-value returned is an approximation.
    '''
    
    x = np.asarray(x)
    y = np.asarray(y)
    
    weights = np.asarray(weights)
    
    weights = weights / np.sum(weights)
    
    x_ranks = weighted_rank(x, weights)
    y_ranks = weighted_rank(y, weights)
    
    mean_x_rank = np.sum(weights * x_ranks)
    mean_y_rank = np.sum(weights * y_ranks)
    
    cov_xy = np.sum(weights * (x_ranks - mean_x_rank) * (y_ranks - mean_y_rank))
    
    var_x = np.sum(weights * (x_ranks - mean_x_rank)**2)
    var_y = np.sum(weights * (y_ranks - mean_y_rank)**2)
    
    correlation = cov_xy / np.sqrt(var_x * var_y) if var_x > 0 and var_y > 0 else 0
    
    n_effective = 1.0 / np.sum(weights**2)
    z = 0.5 * np.log((1 + correlation) / (1 - correlation)) if abs(correlation) < 1 else 0
    p_value = 2 * (1 - stats.norm.cdf(abs(z) * np.sqrt(n_effective - 3)))
    
    return correlation, p_value

def weighted_rank(x, weights):
    """
    Compute weighted ranks for an array.
    """
    sorted_indices = np.argsort(x)
    sorted_weights = weights[sorted_indices]
    sorted_x = x[sorted_indices]
    
    ranks = np.zeros_like(x, dtype=float)
    
    i = 0
    while i < len(x):
        j = i
        while j < len(x) and sorted_x[j] == sorted_x[i]:
            j += 1
            
        if j > i + 1:
            rank_sum = 0
            for k in range(i, j):
                rank_sum += np.sum(sorted_weights[:k]) + sorted_weights[k] / 2
                
            avg_rank = rank_sum / (j - i)
            ranks[sorted_indices[i:j]] = avg_rank
        else:
            ranks[sorted_indices[i]] = np.sum(sorted_weights[:i]) + sorted_weights[i] / 2
            
        i = j
    
    return ranks