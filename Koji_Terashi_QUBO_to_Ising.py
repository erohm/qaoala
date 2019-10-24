import sys, os
import qulacs

import openfermion as of

from openfermion.transforms import get_fermion_operator, jordan_wigner
from openfermion.transforms import get_sparse_operator
from openfermion.hamiltonians import MolecularData
#from openfermionpsi4 import run_psi4

from scipy.optimize import minimize
import numpy as np
#import matplotlib.pyplot as plt


# ==== RUN CONFIG
args = sys.argv
arg_frac = args[1]
arg_maxiter = int(args[2])
print("frac=",arg_frac,", maxiter=",arg_maxiter)


file_r = 'Q_'+arg_frac+'pct.txt'
from ast import literal_eval
with open(file_r, "r") as f:
    line = f.read()
    Q = literal_eval(line)
print("Q size =",len(Q))


nvar = 0
key_i = []
b_ij = np.zeros((100,100))
for (k1, k2), v in Q.items():
#    print(k1,k2,v)
    if k1 == k2: 
        b_ij[nvar][nvar] = v
        key_i.append(k1)
        nvar += 1
for (k1, k2), v in Q.items():
    if k1 != k2: 
        for i in range(nvar):
            for j in range(nvar):
                if k1 == key_i[i] and k2 == key_i[j]:
                    if i < j:
                        b_ij[i][j] = v
                    else:
                        b_ij[j][i] = v

hamil = of.QubitOperator()

J_ij = np.zeros((nvar,nvar))
h_i = np.zeros(nvar)
for i in range(nvar):
    for j in range(nvar):
        if i >= j:
            continue        
        J_ij[i][j] = b_ij[i][j]
        if J_ij[i][j] == 0:
            continue
        hamil += of.QubitOperator(((i,'Z'), (j,'Z')),J_ij[i][j])

for i in range(nvar):
    bias = 0
    for k in range(nvar):
        bias += b_ij[i][k]+b_ij[k][i]
    bias *= -1
    h_i[i] = bias
    if h_i[i] == 0:
        continue
    hamil += of.QubitOperator((i,'Z'),h_i[i])


import time
start_time = time.time()

from qulacs import Observable
from qulacs.observable import create_observable_from_openfermion_text
qulacs_hamiltonian = create_observable_from_openfermion_text(str(hamil))

from qulacs import QuantumState, QuantumCircuit
from qulacs.gate import CZ, RY, RZ, merge, Measurement


def ansatz_circuit(n_qubit, depth, theta_list):
    circuit = QuantumCircuit(n_qubit)
    
    for i in range(n_qubit):
        circuit.add_gate(RY(i, theta_list[i]))
    for d in range(depth):
        for i in range(1,n_qubit):
            circuit.add_H_gate(i)
        for j in range(n_qubit-1):
            circuit.add_CNOT_gate(j, j+1)
            circuit.add_gate(RY(j, theta_list[n_qubit*(1+d)+j]))
            circuit.add_H_gate(j+1)        
        circuit.add_gate(RY(n_qubit-1, theta_list[n_qubit*(1+d)+n_qubit-1]))
    
    return circuit


n_qubit = nvar
depth = 2
init_theta_list = np.random.randn(n_qubit*(depth+1))
print("n_qubit =",n_qubit)

input_state = QuantumState(n_qubit)
input_state.set_zero_state()
#input_state.set_Haar_random_state()

def cost(theta_list):
    #input_state.set_zero_state()
    input_state.set_computational_basis(int('0b'+'1'*(n_qubit/2)+'0'*(n_qubit/2),2))
    circ = ansatz_circuit(n_qubit, depth, theta_list)
    circ.update_quantum_state(input_state)
    value = qulacs_hamiltonian.get_expectation_value(input_state)
    print("  cost -->",value)
    return value


method = "COBYLA"
options = {"disp": False, "maxiter": arg_maxiter}
opt = minimize(cost, init_theta_list, method=method, options=options)

print("opt.x =",opt.x)
print(opt.success,opt.status,opt.message,opt.fun)


circ = ansatz_circuit(n_qubit, depth, opt.x)
for i in range(n_qubit):
    circ.add_gate(Measurement(i,i))

input_state = QuantumState(n_qubit)
#input_state.set_zero_state()
input_state.set_computational_basis(int('0b'+'1'*(n_qubit/2)+'0'*(n_qubit/2),2))
circ.update_quantum_state(input_state)
print("Energy =",qulacs_hamiltonian.get_expectation_value(input_state))


exec_time = time.time() - start_time
print('')
print('QUBO of size '+str(len(Q))+' sampled in '+str(exec_time)+' s')

samples = {}
sys.stdout.write("Value=")
for i in range(n_qubit):
    value = input_state.get_classical_value(i)
    samples[key_i[i]] = int(value)
    sys.stdout.write(str(value))
    sys.stdout.write(" ")
    
file_sample = 'samples_'+arg_frac+'pct_maxiter'+str(arg_maxiter)+'.txt'
with open(file_sample, mode='w') as f:
    f.write('{')
    for k, v in samples.items():
        f.write('\''+k+'\': '+str(v)+', ')
    f.write('}\n')
