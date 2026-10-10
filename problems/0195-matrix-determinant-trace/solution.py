import numpy as np
def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	det = 1
	trace = 0
	matrix = np.array(matrix, dtype=float)
	for c in range(len(matrix)):
		pivot = matrix[c][c]
		trace += pivot
	for c in range(len(matrix)):
		pivot = matrix[c][c]
		if pivot == 0:
			for i in range(c+1, len(matrix)):
				if matrix[i][c] != 0:
					matrix[[c, i]] = matrix[[i, c]]
					det *= -1
					break
			else:
				return (0, trace)
		pivot = matrix[c][c]
		for r in range(c+1,len(matrix)):
			factor = matrix[r][c]/pivot
			matrix[r] = matrix[r] - factor * matrix[c]
		det *= pivot
	return (det, trace)