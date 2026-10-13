import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""
	aug = np.column_stack((A,b)).astype(float)
	m, n = aug.shape
	pivotind = 0
	maxrow = pivotind
	sol_vec = [0.0] * m
	for c in range(n-1):
		maxrow = pivotind
		pivot = aug[pivotind][c]
		maxi = abs(aug[pivotind][c])
		for h in range(pivotind+1, m):
			if abs(aug[h][c]) > maxi:
				maxi = abs(aug[h][c])
				maxrow = h
		aug[[pivotind, maxrow]] = aug[[maxrow, pivotind]]
		pivot = aug[pivotind][c]
		if pivot != 0:
			for r in range(pivotind+1, m):
				factor = aug[r][c] / aug[pivotind][c]
				aug[r] = aug[r] - factor * aug[pivotind]
			pivotind += 1
		if pivotind == m:
			break
	for r in range(m-1, -1, -1):
		fin = aug[r][n-1]
		tot = 0
		if r <= m-2:
			for c in range(n-2, r, -1):
				tot += aug[r][c] * sol_vec[c]
		var = (fin - tot) / aug[r][r]
		sol_vec[r] = var
		
	return sol_vec
