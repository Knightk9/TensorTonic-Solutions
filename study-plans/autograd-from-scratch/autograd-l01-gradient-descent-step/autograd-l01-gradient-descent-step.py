import numpy as np

def gradient_descent_step(values: list, gradients: list, learning_rate: float) -> tuple[list, float]:
    """
    Returns a fresh list of updated values and the predicted objective change.
    """
    values = np.array(values,dtype= float)
    
    gradients = np.array(gradients, dtype= float)
    values_next = values - learning_rate*gradients
    loss = np.sum(gradients*(values_next - values))
    
    return (values_next.tolist(), float(loss))
    
