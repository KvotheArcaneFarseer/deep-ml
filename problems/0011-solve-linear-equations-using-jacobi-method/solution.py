import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	q,z = A.shape
	x = np.zeros(z)
	for i in range(n):
		updated_x = np.zeros_like(x)
		for r in range(q):
			total = 0
			for c in range(z):
				if r != c:
					total += A[r][c] * x[c]
			updated_x[r] = (b[r] - total) / A[r][r]
		x = updated_x
	x = np.round(x,4)
	return x