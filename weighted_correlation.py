import numpy as np
import pandas as pd

def weighted_correlation(x, y, weights):
    # Normalize weights
    weights = weights / np.sum(weights)
    
    # Weighted means
    wx_mean = np.sum(weights * x)
    wy_mean = np.sum(weights * y)
    
    # Centered variables
    x_centered = x - wx_mean
    y_centered = y - wy_mean
    
    # Weighted covariance
    numerator = np.sum(weights * x_centered * y_centered)
    denominator = np.sqrt(
        np.sum(weights * x_centered**2) * 
        np.sum(weights * y_centered**2)
    )
    
    return numerator / denominator