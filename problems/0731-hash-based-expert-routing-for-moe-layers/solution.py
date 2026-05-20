import numpy as np

def hash_moe_forward(token_ids, embeddings, expert_weights, num_experts: int) -> np.ndarray:
    """
    Hash-based routing forward pass for an MoE layer.

    Args:
        token_ids: 1D array-like of N integer token IDs
        embeddings: 2D array-like of shape (N, d) of token embeddings
        expert_weights: list of E numpy arrays, each of shape (d, d_out)
        num_experts: number of experts E

    Returns:
        numpy array of shape (N, d_out) with per-token expert outputs.
    """
    token_ids = np.array(token_ids)
    embeddings = np.array(embeddings)
    routing = token_ids % num_experts
    save_out = []
    for i in range(len(token_ids)):
        exmat = expert_weights[routing[i]]
        current_emb = embeddings[i]
        output = current_emb @ exmat
        save_out.append(output)
    return np.array(save_out)
    pass
