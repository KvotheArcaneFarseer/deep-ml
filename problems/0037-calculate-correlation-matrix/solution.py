import numpy as np

def calculate_correlation_matrix(X, Y=None):
	# Your code here
	z = X.shape[1]
	if Y is not None:
		X = np.hstack((X, Y))
	meanlist = []
	dev = []
	sampvar = np.array([])
	stdev = np.array([])
	total = 0
	totalcovar = 0
	for m in range(len(X[0])):
		meanlist.append(np.mean(X[:, m]))
		dev.append(X[:, m] - np.mean(X[:, m]))
	dev = np.array(dev)
	covar = []
	for a in range(len(dev)):
		row = []
		for b in range(len(dev)):
			total = 0
			for i in range(len(dev[0])):
				total += dev[a][i] * dev[b][i]
			row.append(total / (len(dev[0]) - 1))
		covar.append(row)
	for i in range(len(dev)):
		sampvar = np.append(sampvar, (np.sum(dev[i]**2)) / (len(dev[0]) -1))
		stdev = np.append(stdev, np.sqrt(sampvar[i]))
	corr = []
	for a in range(len(stdev)):
		corr_row = []
		for b in range(len(stdev)):
			corr_row.append(covar[a][b] / (stdev[a] * stdev[b]))
		corr.append(corr_row)
	corr = np.array(corr)
	if Y is not None:
		return corr[:z, z:]
	return corr


