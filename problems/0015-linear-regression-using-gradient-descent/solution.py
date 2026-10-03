import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations
    
    Returns:
        Learned weights as a 1D array of shape (n,)
    """
    r, c = X.shape
    theta = np.zeros(c)
    # mse = (np.sum((predictions - y)**2))/r
    for i in range(iterations):
        predictions = X @ theta
        theta = theta - alpha * ((1/r) * X.T @ (predictions - y))
    return theta