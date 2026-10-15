
import numpy as np

def calculate_correlation_matrix(X, Y=None):
    num_x = X.shape[1]

    if Y is not None:
        X = np.hstack((X, Y))

    # Step 1: Center each variable
    means = np.mean(X, axis=0)
    dev = X - means

    # Step 2: Calculate covariance matrix
    n = X.shape[0]
    covar = (dev.T @ dev) / (n - 1)

    # Step 3: Extract standard deviations
    variances = np.diag(covar)
    stdev = np.sqrt(variances)

    # Step 4: Calculate correlation matrix
    corr = covar / np.outer(stdev, stdev)

    # Step 5: Return the requested correlations
    if Y is not None:
        return corr[:num_x, num_x:]

    return corr
