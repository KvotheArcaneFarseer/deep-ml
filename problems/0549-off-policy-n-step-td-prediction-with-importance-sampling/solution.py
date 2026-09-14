import numpy as np

def off_policy_nstep_td(
    episodes: list,
    behavior_policy: list,
    target_policy: list,
    num_states: int,
    num_actions: int,
    n: int,
    alpha: float,
    gamma: float
) -> np.ndarray:
    V = np.zeros(num_states)
    for episode in episodes:
        for t in range(len(episode)):
            Gt = 0
            rh = 1
            curr_state_ind = episode[t][0]
            curr_state = V[curr_state_ind]
            for exp in range(min(n, len(episode) - t)):
                gamma_exp = gamma**exp
                curr_reward = episode[t+exp][2]
                Gt += gamma_exp*curr_reward
                action = episode[t+exp][1]
                state = episode[t+exp][0]
                rh *= target_policy[state][action] / behavior_policy[state][action]
            if t+n < len(episode):
                fin_state_ind = episode[t+n][0]
                bootstrap = V[fin_state_ind]
                Gt += (gamma**n) * bootstrap
            V[curr_state_ind] = curr_state + alpha*rh*(Gt - curr_state)
            
            


                
    """
    Off-policy n-step TD prediction for state values using importance sampling.

    Args:
        episodes: List of episodes, each a list of (state, action, reward) tuples.
        behavior_policy: b(a|s) as 2D list of shape (num_states, num_actions).
        target_policy: pi(a|s) as 2D list of shape (num_states, num_actions).
        num_states: Number of states.
        num_actions: Number of actions.
        n: Number of steps for the n-step return.
        alpha: Learning rate.
        gamma: Discount factor.

    Returns:
        V: numpy array of shape (num_states,) with estimated state values.
    """
    return V