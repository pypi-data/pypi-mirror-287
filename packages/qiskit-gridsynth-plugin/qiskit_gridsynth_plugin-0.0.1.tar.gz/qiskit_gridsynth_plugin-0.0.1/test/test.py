from qiskit import QuantumCircuit
from src.qiskit_gridsynth_plugin.decompose import clifford_t_transpile
circ = QuantumCircuit.from_qasm_file('circ.qasm')
decomposed = clifford_t_transpile(circ, approx_exp=-4)
print(decomposed.qasm())