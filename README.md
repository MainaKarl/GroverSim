# Quantum Project: Practical Quantum Algorithms

## Overview
This project demonstrates practical applications of quantum computing using Python. It includes Grover's algorithm for database search with multiple marked states and quantum teleportation simulation. The project solves the database searching problem using Grover's algorithm, which efficiently finds a marked item in an unsorted database. It uses quantum superposition to search all items simultaneously and amplifies the probability of the correct result through repeated iterations of Grover's oracle and diffusion operator. This makes it exponentially faster than classical search methods for large datasets.

## Features
- **Grover's Algorithm**: Search for multiple marked states in a database with optimal performance.
- **Quantum Teleportation**: Simulate the teleportation of a qubit's state using entanglement.
- **State Visualization**: Visualize the probabilities of quantum states to better understand the system.
- **Modular Design**: Utilities for state initialization, quantum gate operations, and visualizations are included for extensibility.

## File Structure
```plaintext
QuantumProject/
├── algorithms/
│   ├── grover_application.py    # Implements Grover's algorithm with practical use cases
│   ├── teleportation.py         # Simulates quantum teleportation
├── utils/
│   ├── initialization.py        # Utilities for initializing quantum states
│   ├── operations.py            # Quantum gate operations
│   ├── visualization.py         # Visualization tools for quantum states
├── main.py                      # Entry point for the project
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
```

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd QuantumProject
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the project by executing the main script:
```bash
python main.py
```

### Example: Grover's Algorithm
The project demonstrates Grover's algorithm applied to search for multiple marked states. Modify `main.py` to update the number of qubits and marked states as needed:
```python
num_qubits = 3
marked_states = [2, 5]
```

The program will output the probabilities of each state after running the algorithm and visualize the results.

### Example: Quantum Teleportation
Use the `teleportation.py` script to simulate quantum teleportation of a qubit's state.

## Future Work
- Implement Shor's algorithm for integer factorization.
- Extend Grover's algorithm to larger systems.
- Explore hybrid quantum-classical algorithms.

## Dependencies
- Python 3.8+
- NumPy
- Matplotlib

## Contributions
Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests.

## License
This project is licensed under the MIT License.

