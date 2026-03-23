def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# If the matrix is empty, return an empty list
    if len(a) == 0:
        return []

    # Check that the number of columns matches the length of b
    if len(a[0]) != len(b):
        return -1

    result = []

    # Go through each row in the matrix
    for row in a:
        # Extra safety check in case rows have inconsistent lengths
        if len(row) != len(b):
            return -1

        total = 0

        # Compute dot product of this row with b
        for i in range(len(b)):
            total += row[i] * b[i]

        result.append(total)

    return result