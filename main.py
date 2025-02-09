from quantum_grover import grover_algorithm
from utils.visualization import plot_probabilities

# Parameters
n_qubits = 3
marked_states = ["101", "111"]
iterations = 2

# Run Grover's Algorithm
final_state = grover_algorithm(n_qubits, marked_states, iterations)

# Measure and visualize probabilities
from utils.visualization import measure_probabilities
probabilities = measure_probabilities(final_state)
plot_probabilities(probabilities, n_qubits)
