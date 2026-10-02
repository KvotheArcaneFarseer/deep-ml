import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	gradient = np.array(gradient)
	L2 = float(np.linalg.norm(gradient))
	if L2 == 0:
		return {'magnitude':L2, 'direction': list(np.zeros_like(gradient)), 'descent_direction': list(np.zeros_like(gradient))}
	else:
		return {'magnitude':L2, 'direction': list(gradient/L2), 'descent_direction': list(-1 * (gradient / L2))}