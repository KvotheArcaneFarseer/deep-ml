import math
import numpy as np
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	features = np.array(features)
	weights = np.array(weights)
	labels = np.array(labels)
	z = features @ weights + bias
	probabilities = 1/(1+np.exp(-z))
	mse = np.mean((probabilities - labels)**2)
	probabilities = np.round(probabilities, 4)
	mse = np.round(mse, 4)
	return probabilities, mse