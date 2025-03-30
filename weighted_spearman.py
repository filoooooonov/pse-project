import numpy as np
from scipy import stats

def weighted_spearman(x, y, weights=None):
    """
    Calculate the weighted Spearman's rank correlation coefficient.
    
    Parameters:
    -----------
    x : array-like
        First array of data
    y : array-like
        Second array of data
    weights : array-like, optional
        Weights for each observation. If None, uniform weights are used.
        
    Returns:
    --------
    correlation : float
        Weighted Spearman's rank correlation coefficient
    
    p_value : float
        Two-sided p-value for a hypothesis test with null hypothesis
        that two sets of data are uncorrelated
    """

    if weights is None:
        # If no weights provided, use regular Spearman's correlation
        return stats.spearmanr(x, y)
    
    x = np.asarray(x)
    y = np.asarray(y)
    
    
    
    weights = np.asarray(weights)
    
    # Validate inputs
    if len(x) != len(y) or len(x) != len(weights):
        raise ValueError("x, y, and weights must have the same length")
    
    if np.any(weights < 0):
        raise ValueError("Weights cannot be negative")
    
    if np.sum(weights) == 0:
        raise ValueError("Sum of weights cannot be zero")
    
    # Normalize weights to sum to 1
    weights = weights / np.sum(weights)
    
    # Get ranks for x and y
    # We need to handle ties appropriately for weighted ranking
    x_ranks = weighted_rank(x, weights)
    y_ranks = weighted_rank(y, weights)
    
    # Calculate weighted covariance of ranks
    mean_x_rank = np.sum(weights * x_ranks)
    mean_y_rank = np.sum(weights * y_ranks)
    
    cov_xy = np.sum(weights * (x_ranks - mean_x_rank) * (y_ranks - mean_y_rank))
    
    # Calculate weighted variances of ranks
    var_x = np.sum(weights * (x_ranks - mean_x_rank)**2)
    var_y = np.sum(weights * (y_ranks - mean_y_rank)**2)
    
    # Calculate correlation
    correlation = cov_xy / np.sqrt(var_x * var_y) if var_x > 0 and var_y > 0 else 0
    
    # Approximate p-value
    # Note: For weighted correlation, exact p-value calculation is complex
    # This approximation uses Fisher's z-transformation
    n_effective = 1.0 / np.sum(weights**2)  # Effective sample size
    z = 0.5 * np.log((1 + correlation) / (1 - correlation)) if abs(correlation) < 1 else 0
    p_value = 2 * (1 - stats.norm.cdf(abs(z) * np.sqrt(n_effective - 3)))
    
    return correlation, p_value

def weighted_rank(x, weights):
    """
    Compute weighted ranks for an array.
    
    Parameters:
    -----------
    x : array-like
        Array to be ranked
    weights : array-like
        Weights for each observation
        
    Returns:
    --------
    ranks : ndarray
        Weighted ranks for each value in x
    """
    # Sort indices
    sorted_indices = np.argsort(x)
    sorted_weights = weights[sorted_indices]
    sorted_x = x[sorted_indices]
    
    # Initialize ranks
    ranks = np.zeros_like(x, dtype=float)
    
    # Handle ties by giving the average rank
    i = 0
    while i < len(x):
        j = i
        while j < len(x) and sorted_x[j] == sorted_x[i]:
            j += 1
            
        # Calculate the weighted rank for tied values
        if j > i + 1:  # We have ties
            # Calculate the weighted average of ranks for this tied group
            rank_sum = 0
            for k in range(i, j):
                rank_sum += np.sum(sorted_weights[:k]) + sorted_weights[k] / 2
                
            avg_rank = rank_sum / (j - i)
            ranks[sorted_indices[i:j]] = avg_rank
        else:  # No ties
            # The rank is the sum of weights of smaller values plus half the weight of the current value
            ranks[sorted_indices[i]] = np.sum(sorted_weights[:i]) + sorted_weights[i] / 2
            
        i = j
    
    return ranks

# Example usage
if __name__ == "__main__":
    # Sample data
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 5, 4, 1])
    weights = np.array([0.1, 0.2, 0.4, 0.2, 0.1])
    
    # Calculate weighted Spearman correlation
    corr, p_value = weighted_spearman(x, y, weights)
    print(f"Weighted Spearman correlation: {corr:.4f}")
    print(f"P-value: {p_value:.4f}")
    
    # Compare with regular Spearman correlation
    regular_corr, regular_p = stats.spearmanr(x, y)
    print(f"Regular Spearman correlation: {regular_corr:.4f}")
    print(f"Regular P-value: {regular_p:.4f}")