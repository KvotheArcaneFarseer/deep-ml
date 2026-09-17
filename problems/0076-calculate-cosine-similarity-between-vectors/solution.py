import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	magnitude1 = np.sqrt(np.sum(v1**2))
	magnitude2 = np.sqrt(np.sum(v2**2))
	if (v1.size != 0 and v2.size != 0) and (magnitude1 != 0 and magnitude2 != 0):
		if v1.shape == v2.shape:
			cos = float((v1 @ v2)/ (magnitude1 * magnitude2))
			return cos

	pass