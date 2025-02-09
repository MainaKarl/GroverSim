from algorithms.grover_application import grover_search
from utils.initialization import initialize_superposition

def main():
    # Example: Practical application of Grover's algorithm
    num_qubits = 3
    marked_states = [2, 5]  # Marked states in the search space
    print(f"Running Grover's Algorithm with marked states: {marked_states}")
    
    final_state = grover_search(marked_states, num_qubits)
    print(f"Final state probabilities: {abs(final_state)**2}")

if __name__ == "__main__":
    main()
