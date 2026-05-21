def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	output = []
	if mode == 'column':
		for col in range(len(matrix[0])):
			total = 0;
			for row in range(len(matrix)):
				total += matrix[row][col];
				means = total / len(matrix);
			output.append(means);
	else:
		for row in range(len(matrix)):
			total = 0;
			for col in range(len(matrix[0])):
				total += matrix[row][col];
				means = total / len(matrix[0]);
			output.append(means);

	return output