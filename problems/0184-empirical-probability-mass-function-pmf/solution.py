def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    distinct = sorted(set(samples))
    answer = []
    for i in distinct:
        freq = samples.count(i)
        prob = freq / len(samples)
        answer.append((i, prob))
    return answer
    
