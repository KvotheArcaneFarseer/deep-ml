import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    """
    Check if a set of vectors is linearly independent.
    
    Args:
        vectors: List of vectors, where each vector is a list of floats.
                 All vectors must have the same dimension.
        
    Returns:
        True if vectors are linearly independent, False otherwise.
    """
    vectors = np.array(vectors, dtype=float)
    pivotind = 0
    if len(vectors) == 0:
        return True
    for c in range(len(vectors[0])):
        if pivotind == len(vectors):
            break
        pivot = vectors[pivotind][c]
        if pivot == 0:
            for h in range(pivotind, len(vectors)):
                if vectors[h][c] != 0:
                    vectors[[pivotind, h]] = vectors[[h, pivotind]]
                    break
        pivot = vectors[pivotind][c]
        if pivot != 0:
            for r in range(pivotind+1, len(vectors)):
                factor = vectors[r][c] / vectors[pivotind][c]
                vectors[r] = vectors[r] - factor * vectors[pivotind]
            pivotind += 1
    if len(vectors) > pivotind:
        return False
    else:
        return True