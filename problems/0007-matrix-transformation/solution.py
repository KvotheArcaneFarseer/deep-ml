import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	Aarr = np.array(A)
	Tarr = np.array(T)
	Sarr = np.array(S)
	if np.isclose(np.linalg.det(Tarr),0) or np.isclose(np.linalg.det(Sarr),0):
		return -1
	else:
		transformed_matrix = np.linalg.inv(Tarr) @ Aarr @ Sarr
		return transformed_matrix.tolist()