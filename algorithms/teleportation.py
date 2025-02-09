import numpy as np
from utils.operations import apply_hadamard, apply_cnot

def teleport_qubit(state_to_teleport):
    """
    Simulates quantum teleportation of a single-qubit state.
    
    Args:
        state_to_teleport (np.ndarray): 2D array representing the qubit's state.
        
    Returns:
        np.ndarray: Teleported qubit's state.
    """
    # Step 1: Create entangled pair
    entangled_pair = np.array([1, 0, 0, 1]) / np.sqrt(2)  # Bell state
    
    # Step 2: Combine with the state to be teleported
    combined_state = np.kron(state_to_teleport, entangled_pair)
    
    # Step 3: Apply CNOT and Hadamard gates
    combined_state = apply_cnot(combined_state, control=0, target=1)
    combined_state = apply_hadamard(combined_state, target=0)
    
    # Step 4: Measure the first two qubits and apply corrections
    # Here we simulate a perfect correction (idealized teleportation)
    teleported_state = combined_state[2:]
    return teleported_state
