import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    data = np.array(data)
    mean = np.mean(data)
    median = np.median(data)
    freqlist = {}
    for i in range(len(data)):
        freq = 1
        if data[i] not in freqlist:
            freqlist[data[i]] = freq
        else:
            freqlist[data[i]] += 1
    mode = max(freqlist, key=freqlist.get)
    var = np.mean((data-mean)**2)
    stdev = np.std(data)
    q1, q2, q3 = np.percentile(data, [25, 50, 75])
    iqr = q3 - q1
    return {'mean': mean, 'median': median, 'mode' : mode, 'variance': var, 'standard_deviation': stdev, '25th_percentile': q1, '50th_percentile': q2, '75th_percentile': q3, 'interquartile_range': iqr}


