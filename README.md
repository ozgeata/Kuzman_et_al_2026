# Kuzman_et_al_2026
In this study, we introduced the bacterial RuMP cycle as the sole methanol assimilation pathway in K. phaffii. pFBA shows the differences in ATP requirements and fluxes in both strains. This repository contains the Python implementation for our paper. Our Zenodo DOI for the code used for our analysis is: 
https://doi.org/10.5281/zenodo.18837996


## 🛠 Software Requirements

This analysis was developed and tested using:
- **Python:** 3.8+
- **COBRApy:** v0.30.0
- **Primary Solver:** GLPK (GNU Linear Programming Kit)

### 🧩 Solver Information
The scripts are configured to use the **GLPK** solver. If you have **Gurobi** or **CPLEX** installed, COBRApy will detect them automatically, but GLPK is sufficient to reproduce the results in this paper.


### 🏃 How to Run
Once the environment is activated and requirements are installed, execute the main analysis:

```bash
python Kuzman_et_al.py


