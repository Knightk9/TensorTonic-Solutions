import numpy as np

def wasserstein_critic_loss(real_scores: list, fake_scores: list) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    real_scores = np.array(real_scores)
    fake_scores = np.array(fake_scores)
    real = np.mean(real_scores)
    fake = np.mean(fake_scores)
    return (fake - real).item()