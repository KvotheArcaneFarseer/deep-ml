import numpy as np
def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	dice = np.arange(1, n+1)
	mean = np.mean(dice)
	EX = 0
	for i in range(1, n+1):
		EX += (1/n) * i
	var = np.mean((dice - EX)**2)
	return (EX,var)