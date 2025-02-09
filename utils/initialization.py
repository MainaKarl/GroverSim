import numpy as np

def initialize_superposition(num_qubits):
    """
    Creates a uniform superposition state for a given number of qubits.
    
    Args:
        num_qubits (int): Number of qubits.
        
    Returns:
        np.ndarray: State vector.
    """
    num_states = 2**num_qubits
    return np.ones(num_states) / np.sqrt(num_states)

def validate_state(state):
    """
    Validates that the state vector is normalized.
    
    Args:
        state (np.ndarray): State vector.
        
    Raises:
        ValueError: If the state is not normalized.
    """
    norm = np.linalg.norm(state)
    if not np.isclose(norm, 1.0):
        raise ValueError("State vector is not normalized.")
