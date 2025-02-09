import matplotlib.pyplot as plt
import numpy as np

def measure_probabilities(state):
    return np.abs(state)**2

def plot_probabilities(probabilities, n_qubits):
    states = [bin(i)[2:].zfill(n_qubits) for i in range(2**n_qubits)]
    plt.bar(states, probabilities)
    plt.xlabel("States")
    plt.ylabel("Probability")
    plt.title("State Probabilities After Grover's Algorithm")
    plt.xticks(rotation=90)
    plt.show()
