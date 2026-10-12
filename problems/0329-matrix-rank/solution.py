import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    m, n = A.shape
    pivotind = 0
    for c in range(n):
        pivot = A[pivotind][c]
        if abs(pivot) <= tol:
            for h in range(pivotind, m):
                if abs(A[h][c]) > 0:
                    A[[pivotind, h]] = A[[h,pivotind]]
                    break
        pivot = A[pivotind][c]
        if abs(pivot) > tol:
            for r in range(pivotind+1, m):
                factor = A[r][c] / pivot
                A[r] = A[r] - factor * A[pivotind]
            pivotind += 1
        if pivotind == m:
            break
    return pivotind
        
        