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


## 🧪 Simulation Parameters & pFBA Conditions

To ensure reproducibility, the Parsimonious Flux Balance Analysis (pFBA) was performed using the following standardized constraints and parameters:

### 1. Metabolic Constraints
* **Objective Function:** Maximization of biomass production (Ex_biomass).
* **Non-Growth Associated Maintenance (NGAM):** Held constant at **[Insert Value, e.g., 8.39]** $mmol \cdot g_{DW}^{-1} \cdot h^{-1}$ to represent baseline cellular maintenance.
* **Carbon Source:** Methanol was provided as the primary carbon and energy source, with uptake rates constrained to match experimental chemostat observations.

### 2. Comparative Analysis (Wild-Type vs. RuMPi)
The energetic efficiency of the RuMPi strain was compared to the wild-type by simulating growth across a range of methanol uptake rates:
* **Methanol Uptake Range:** [Insert Min] to [Insert Max] $mmol \cdot g_{DW}^{-1} \cdot h^{-1}$.
* **Steady-State Assumption:** All simulations assume metabolic steady-state using pFBA (parsimonious Flux Balance Analysis) to minimize total enzymatic investment.

[Image of Flux Balance Analysis constraints and objective function diagram]

### 3. ATP Expenditure Calculation
ATP consumption rates were quantified by identifying all reactions where ATP is a reactant. The specific consumption for each reaction was calculated using the absolute flux value and its stoichiometric coefficient:
> **Total ATP Demand = |Flux| × |ATP Stoichiometry|**

This calculation explicitly partitions energy usage into:
1. **Growth-Associated Maintenance (GAM):** Energy required for macromolecular synthesis (embedded in the biomass reaction).
2. **Maintenance (NGAM):** Fixed energetic costs for homeostasis.
3. **Pathway-Specific Usage:** ATP consumed by individual metabolic steps in the methanol assimilation pathway.
