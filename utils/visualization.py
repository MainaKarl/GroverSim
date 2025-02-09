import numpy as np
import matplotlib.pyplot as plt

def plot_probabilities(state, title="Quantum State Probabilities"):
    """
    Plots the probabilities of measuring each state.
    
    Args:
        state (np.ndarray): State vector.
        title (str): Title of the plot.
    """
    probabilities = np.abs(state)**2
    plt.bar(range(len(probabilities)), probabilities)
    plt.title(title)
    plt.xlabel("State")
    plt.ylabel("Probability")
    plt.show()
