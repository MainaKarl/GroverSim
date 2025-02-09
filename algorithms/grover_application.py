import numpy as np
from utils.operations import apply_hadamard, apply_oracle, apply_diffuser
from utils.visualization import plot_probabilities

def grover_search(marked_states, num_qubits):
    """
    Grover's algorithm to search for multiple marked states in a database.
    
    Args:
        marked_states (list): List of marked states as integers.
        num_qubits (int): Number of qubits in the system.
        
    Returns:
        np.ndarray: Final state vector after the search.
    """
    num_states = 2**num_qubits
    # Initialize uniform superposition state
    state = np.ones(num_states) / np.sqrt(num_states)
    
    # Create oracle and diffuser
    oracle = apply_oracle(marked_states, num_states)
    diffuser = apply_diffuser(num_states)
    
    # Number of iterations (Grover's optimal number)
    num_iterations = int(np.pi / 4 * np.sqrt(num_states / len(marked_states)))
    
    # Apply Grover's iterations
    for _ in range(num_iterations):
        state = oracle @ state
        state = diffuser @ state
    
    # Visualize the probabilities
    plot_probabilities(state, title="Grover's Algorithm Probabilities")
    return state
