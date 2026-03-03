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


## 🧪 Simulation Parameters & pFBA Conditions

To ensure reproducibility, the Parsimonious Flux Balance Analysis (pFBA) was performed using the following standardized constraints and parameters:

### 1. Metabolic Constraints
* **Objective Function:** Maximization of biomass production (Ex_biomass).
* **Non-Growth Associated Maintenance (NGAM):** Held constant at **0.4** $mmol \cdot g_{DW}^{-1} \cdot h^{-1}$ to represent baseline cellular maintenance. But for growth on glycerol and glucose, it should be adjusted.
* **Carbon Source and Environmental Conditions:** Environmental conditions for growth on glucose, glycerol and methanol were provided. For pFBA analysis, methanol was provided as the primary carbon and energy source, with uptake rates constrained to match experimental chemostat observations. Setting the environmental conditions for methanol allows to use the respective biomass composition. 


### 2. Comparative Analysis (Wild Type vs. RuMPi)
The energetic efficiency of the RuMPi strain was compared to the wild-type by simulating growth across a range of methanol uptake rates:
* **Methanol Uptake Range:** 1.5 to 5 $mmol \cdot g_{DW}^{-1} \cdot h^{-1}$.
* **Steady-State Assumption:** All simulations assume metabolic steady-state using pFBA to minimize total enzymatic investment.

### 3. ATP Expenditure Calculation
ATP consumption rates were quantified by identifying all reactions where ATP is a reactant. ATP in different organelles were considered during calculations (atp_c, atp_m, atp_x, ...). The specific consumption for each reaction was calculated using the absolute flux value and its stoichiometric coefficient:
> **Total ATP Demand = |Flux| × |ATP Stoichiometry|**


This calculation explicitly partitions energy usage into:
1. **Growth-Associated Maintenance (GAM):** Energy required for macromolecular synthesis (embedded in the biomass reaction).
2. **Maintenance (NGAM):** Fixed energetic costs for maintenance.
3. **Total ATP demand:** Total ATP consumed by the metabolism. 

### 🏃 How to Run
Once the environment is activated and requirements are installed, execute the main analysis:

```bash
python Kuzman_et_al.py


