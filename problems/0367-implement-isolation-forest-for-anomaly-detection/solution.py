import numpy as np
import math

def isolation_forest(X, n_trees=10, sample_size=4, random_state=None):
    rng = np.random.RandomState(random_state)
    n_samples = X.shape[0]
    max_depth = math.ceil(math.log2(sample_size))

    def c_factor(n):
        if n <= 1:
            return 0.0
        return 2.0 * (np.log(n - 1) + 0.5772156649) - 2.0 * (n - 1) / n

    def build_tree(data, depth):
        """Returns a tree as a dict (node) or leaf size (int)."""
        n = len(data)
        if n <= 1 or depth >= max_depth:
            return n  # leaf: store size for c_factor adjustment
        
        feature = rng.randint(0, data.shape[1])
        min_val = data[:, feature].min()
        max_val = data[:, feature].max()
        
        if min_val == max_val:
            return n  # can't split, treat as leaf
        
        split = rng.uniform(min_val, max_val)
        left_data = data[data[:, feature] <= split]
        right_data = data[data[:, feature] > split]
        
        return {
            'feature': feature,
            'split': split,
            'left': build_tree(left_data, depth + 1),
            'right': build_tree(right_data, depth + 1),
        }

    def traverse(node, point, depth):
        """Deterministically traverse a built tree for a given point."""
        if isinstance(node, int):  # leaf node
            return depth + c_factor(node)
        
        if point[node['feature']] <= node['split']:
            return traverse(node['left'], point, depth + 1)
        else:
            return traverse(node['right'], point, depth + 1)

    path_lengths = np.zeros((n_samples, n_trees))
    
    for t in range(n_trees):
        indices = rng.choice(n_samples, size=sample_size, replace=False)
        sample = X[indices]
        tree = build_tree(sample, 0)  # all rng calls happen here
        
        for i in range(n_samples):
            path_lengths[i, t] = traverse(tree, X[i], 0)  # no rng here

    avg_path_length = path_lengths.mean(axis=1)
    c_n = c_factor(sample_size)
    scores = 2 ** (-avg_path_length / c_n)
    return scores