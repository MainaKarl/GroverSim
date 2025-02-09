import numpy as np

def apply_hadamard(state, target):
    """
    Applies a Hadamard gate to a specific qubit in the state vector.
    
    Args:
        state (np.ndarray): State vector.
        target (int): Target qubit index.
        
    Returns:
        np.ndarray: Updated state vector.
    """
    num_qubits = int(np.log2(len(state)))
    H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    full_gate = np.eye(1)
    for i in range(num_qubits):
        full_gate = np.kron(full_gate, H if i == target else np.eye(2))
    return full_gate @ state

def apply_oracle(marked_states, num_states):
    """
    Constructs the oracle for Grover's algorithm.
    """
    oracle = np.eye(num_states)
    for state in marked_states:
        oracle[state, state] = -1
    return oracle

def apply_diffuser(num_states):
    """
    Constructs the diffuser operator for Grover's algorithm.
    """
    H = np.ones((num_states, num_states)) / num_states
    return 2 * H - np.eye(num_states)
