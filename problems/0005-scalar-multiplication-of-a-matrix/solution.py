def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	output = []
	
	for row in matrix:
		new_row = []
		for el in row:
			new_row.append(el * scalar)
		output.append(new_row)
	return output
	pass