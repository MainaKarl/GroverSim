import numpy as np

def initialize_state(n_qubits):
    state = np.ones(2**n_qubits) / np.sqrt(2**n_qubits)
    return state

def apply_oracle(state, n_qubits, marked_states):
    for marked in marked_states:
        index = int(marked, 2)
        state[index] *= -1
    return state

def apply_diffusion_operator(state, n_qubits):
    mean_amplitude = np.mean(state)
    return 2 * mean_amplitude - state

def grover_algorithm(n_qubits, marked_states, iterations):
    state = initialize_state(n_qubits)
    for _ in range(iterations):
        state = apply_oracle(state, n_qubits, marked_states)
        state = apply_diffusion_operator(state, n_qubits)
    return state
