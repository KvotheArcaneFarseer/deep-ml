import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	q,z = data.shape
	standardized_data = []
	normalized_data = []
	for i in range(z):
		avg = np.mean(data[:,i])
		stdev = np.std(data[:,i])
		maxi = data[:,i].max()
		mini = data[:,i].min()
		standar = (data[:, i] - avg) / stdev
		mmnormalized = (data[:, i] - mini) / (maxi - mini)
		standardized_data.append(standar)
		normalized_data.append(mmnormalized)
	standardized_data = (np.array(standardized_data)).T
	normalized_data = (np.array(normalized_data)).T
	return standardized_data, normalized_data