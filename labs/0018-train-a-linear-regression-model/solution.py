import numpy as np

def train(X, y, W, b):
    """
    Train linear regression weights on standardized data.
    
    Args:
        X: numpy array of shape (n_samples, n_features) -- standardized features
        y: numpy array of shape (n_samples,) -- standardized targets
        W: numpy array of shape (n_features,) -- initial random weights
        b: float -- initial bias (0.0)
    
    Returns:
        W: numpy array of shape (n_features,) -- trained weights
        b: float -- trained bias
    """
    # TODO: implement your training strategy here
    # You can use ANY approach: gradient descent, normal equation,
    # momentum, adaptive learning rates, mini-batching, etc.
    n_samples, n_features = X.shape
    learning_rate = 0.01
    num_epochs = 1000
    batch_size = 32
    for epoch in range(num_epochs):
        indices = np.random.permutation(n_samples)
        X_shuffled = X[indices]
        y_shuffled = y[indices]
        for start in range(0, n_samples, batch_size):
            end = start + batch_size
            X_batch = X_shuffled[start:end]
            y_batch = y_shuffled[start:end]
            y_pred = X_batch @ W + b
            error = y_pred - y_batch
            grad_W = (2 / len(X_batch)) * (X_batch.T @ error)
            grad_b = 2 * np.mean(error)
            W = W - learning_rate * grad_W
            b = b - learning_rate * grad_b
    return W, b


        #shuffle data
        #predict
        #compute errors
        #compuete gradients
        #update weights
    pass
