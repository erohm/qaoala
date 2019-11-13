
```                              
 ,adPPPYba,                                                        |                |                                
a8"      "8a.  ,adPPYYba,                                          |                |
88         88  ""     `Y8                       _____              |   ______       |
88         88  ,adPPPPP88                      /     \________________/      \      |
"8a,    \ \8"  88,    ,88                     /      /                \       \     |                                     
 `"YbbdbP\_\   `"8bbdP"Y8                    |  ( ) /                  \ ( )  |     |
                                              \    /   ~~~        ~~~   \    /      |
  ,adPPYba,    ,adPPYYba,                      \__|                      |__/       |
 a8"     "8a   ""     `Y8                         |   ( @ )  / \ ( @ )   |       {___)
 8b       d8   ,adPPPPP88                         |         (   )        |      {____)
 "8a,   ,a8"   88,    ,88                          \         \ /         /       {___)
  `"YbbdP"'    `"8bbdP"Y8                 <(*)>     \    ===\___/===    /         {__)
                                          \_\_\___   \_________________/            |
    88         ,adPPYYba,                        \ \       /        |               |
    88         ""     `Y8                         \ \____/          |               |
    88         ,adPPPPP88                          \____/           |               |
    88         88,    ,88                              (            |               |
    88888888   `"8bbdP"Y8                               (           |               |
                                                         \__________|               |
                                                                       
```
# Qaoala
This codebase is part of the [HEP.QPR](https://hep-qpr.lbl.gov/) project and is built on [Qallse](https://github.com/derlin/hepqpr-qallse). Qaoala encodes charged particle track pattern recognition problems from the [TrackML](https://www.kaggle.com/c/trackml-particle-identification/data) dataset into a form which can be solved using a Quantum Approximate Optimization Algorithm (QAOA)on a gate-based machine. 

### Dependencies 
In order to use Qaoala, you will need to [install Qallse](https://github.com/derlin/hepqpr-qallse#setup-and-usage), [install EntropicaQAOA](https://docs.entropicalabs.io/qaoa/#installation), [download the Rigetti Forrest SDK](https://www.rigetti.com/forest) and [install PyQuil](http://docs.rigetti.com/en/stable/start.html#start). Qallse recommneds creating a virtual environment. Though this may not be compatible with Rigetti and EntropicaQAOA, we bypass this by exporting the QUBO file generated from Qallse.   

```
git clone <this repo>
cd <dir>
```
### Quantum Approximate Optimization Algorithm
Proposed by [Farhi et al. in 2014](https://arxiv.org/pdf/1411.4028.pdf), a Quantum Approximate Optimization Algorithm (QAOA) is a hybrid quantum-classical method of approximately solving certain optimization problems. This approach is particularly advantageous in the NISQ era and beyond, since it relies on classical optimizers to help steer the quantum computation. In QAOA, the primary goal is to minimize a set of two n-length parameters which together parameterize a cost function. In a quantum circuit, the cost function is evaluated to produce a cost value, which is the expectation value of the cost function. This cost value is then classically optimized to indicate whether the quantum varying is in a direction of greater or lesser cost. These "updated" parameters are then returned to the quantum circuit for re-evaluation. This process repeats over p iterations corresponding to circuit depth. For successful QAOA, accuracy increases with p iterations.    


