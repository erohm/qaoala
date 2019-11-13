
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
Qaoala is built on Qallse and EntropicaQAOA. In order to use this, you will need to [install Qallse](https://github.com/derlin/hepqpr-qallse#setup-and-usage), [install EntropicaQAOA](https://docs.entropicalabs.io/qaoa/#installation), [download the Rigetti Forrest SDK](https://www.rigetti.com/forest) and [install PyQuil](http://docs.rigetti.com/en/stable/start.html#start). Qallse recommneds creating a virtual environment. Though this may not be compatible with Rigetti and EntropicaQAOA, we bypass this by exporting the QUBO file generated from Qallse.  


