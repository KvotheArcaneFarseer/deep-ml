import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	x = np.array(X)
	y = np.array(y)
	parameters = np.linalg.inv(x.T @ x) @ x.T @ y
	theta = np.round(parameters, 4)
	return theta.tolist()