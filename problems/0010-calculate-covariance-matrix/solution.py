def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	overdev = []
	covmat = []
	for vec in vectors:
		total = 0
		deviation = []
		for rowvec in vec:
			total += rowvec
		mean = total / len(vec)
		for rowvec in vec:
			deviation.append(rowvec - mean)
		overdev.append(deviation)
	for i in range(len(overdev)):
		row = []
		for j in range(len(overdev)):
			total = 0
			for k in range(len(overdev[i])):
				total += overdev[i][k] * overdev[j][k]
			cov = total / (len(overdev[i]) - 1)
			row.append(cov)
		covmat.append(row)
	return covmat
		




		
	return []