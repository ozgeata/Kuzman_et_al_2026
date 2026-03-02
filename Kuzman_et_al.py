#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cobra
import pandas as pd


# In[2]:


#Add the path of the model
model_path='/....../MODEL1612130000_url.xml'
model=cobra.io.read_sbml_model(model_path)
model


# In[11]:


#Addition of peroxisomal transaldolase
from cobra import Reaction, Metabolite

g3p_x = model.metabolites.get_by_id("g3p_x")
s7p_x = model.metabolites.get_by_id("s7p_x")
e4p_x = model.metabolites.get_by_id("e4p_x")
f6p_x = model.metabolites.get_by_id("f6p_x")

if "TALx" in model.reactions:
    r_TALx = model.reactions.get_by_id("TALx")
else:
    r_TALx = Reaction("TALx")
    r_TALx.name = "transaldolase peroxisomal"
    r_TALx.lower_bound = 0     
    r_TALx.upper_bound = 1000.0

    r_TALx.add_metabolites({
        g3p_x: 1.0,    
        f6p_x: -1.0, 
        s7p_x: 1.0,
        e4p_x: -1.0
         
    })

    model.add_reactions([r_TALx])

r_TALx.gene_reaction_rule = "TAL1-2"


# In[12]:


#Addition of RuMP reactions_HPS

from cobra import Reaction, Metabolite


fald_x = model.metabolites.get_by_id("fald_x")
ru5p_D_x = model.metabolites.get_by_id("ru5p_D_x")
f6p_x = model.metabolites.get_by_id("f6p_x")


if "h6p_x" in model.metabolites:
    h6p_x = model.metabolites.get_by_id("h6p_x")
else:
    h6p_x = Metabolite(
        id="h6p_x",
        name="Hexulose 6-phosphate (peroxisome)",
        compartment="x"
    )
    model.add_metabolites([h6p_x])


if "h6p_synth" in model.reactions:
    r_h6p_synth = model.reactions.get_by_id("h6p_synth")
else:
    r_h6p_synth = Reaction("h6p_synth")
    r_h6p_synth.name = "h6p_synthase"
    r_h6p_synth.lower_bound = 1.0      
    r_h6p_synth.upper_bound = 1000.0

    r_h6p_synth.add_metabolites({
        fald_x: -1.0,    
        ru5p_D_x: -1.0,    
        h6p_x: 1.0   
    })

    r_h6p_synth.gene_reaction_rule = "HPS"


model.add_reactions([r_h6p_synth])


# In[13]:


#Addition of RuMP reactions_PHI

from cobra import Reaction, Metabolite


fald_x = model.metabolites.get_by_id("fald_x")
ru5p_D_x = model.metabolites.get_by_id("ru5p_D_x")
f6p_x = model.metabolites.get_by_id("f6p_x")
h6p_x = model.metabolites.get_by_id("h6p_x")


if "h6p_iso" in model.reactions:
    r_h6p_iso = model.reactions.get_by_id("h6p_iso")
else:
    r_h6p_iso = Reaction("h6p_iso")
    r_h6p_iso.name = "h6p_isomerase"
    r_h6p_iso.lower_bound = 1     
    r_h6p_iso.upper_bound = 1000.0

    r_h6p_iso.add_metabolites({
        h6p_x: -1.0,    
        f6p_x: 1.0,    
         
    })

    model.add_reactions([r_h6p_iso])


r_h6p_iso.gene_reaction_rule = "PHI"


# In[14]:


#Assigning TKL1 for DAS deletion in RuMP strain
rxn = model.reactions.get_by_id("TKT1x")
rxn.gene_reaction_rule = "TKL1"


# In[15]:


#Assigning TKL1 for DAS deletion in RuMP strain
rxn = model.reactions.get_by_id("TKT2x")
rxn.gene_reaction_rule = "TKL1"


# In[16]:


#Environmental conditions for each carbon source
                
envcond_gly={'Ex_glyc':(-2.41,0),
             'Ex_glc_D':(0,0),
             'Ex_meoh':(0,0),
             'ATPM':(2.51,2.51),
             'BIOMASS_glyc':(0,1000),
             'PROTEINS_glyc':(0,1000),
             'LIPIDS_glyc':(0,1000),
             'STEROLS_glyc':(0,1000),
             'BIOMASS':(0,0),
             'PROTEINS':(0,0),
             'LIPIDS':(0,0),
             'STEROLS':(0,0),
             'BIOMASS_meoh':(0,0),
             'PROTEINS_meoh':(0,0),
             'LIPIDS_meoh':(0,0),
             'STEROLS_meoh':(0,0)}

envcond_glu={'Ex_glyc':(0,0),
             'Ex_glc_D':(-1.02,0),
             'Ex_meoh':(0,0),
             'ATPM':(2.81,2.81),
             'BIOMASS_glyc':(0,0),
             'PROTEINS_glyc':(0,0),
             'LIPIDS_glyc':(0,0),
             'STEROLS_glyc':(0,0),
             'BIOMASS':(0,1000),
             'PROTEINS':(0,1000),
             'LIPIDS':(0,1000),
             'STEROLS':(0,1000),
             'BIOMASS_meoh':(0,0),
             'PROTEINS_meoh':(0,0),
             'LIPIDS_meoh':(0,0),
             'STEROLS_meoh':(0,0)}
                
envcond_meoh={'Ex_glyc':(0,0),
             'Ex_glc_D':(0,0),
             'Ex_meoh':(-1.5,0),
             'ATPM':(0.4,0.4),
             'BIOMASS_glyc':(0,0),
             'PROTEINS_glyc':(0,0),
             'LIPIDS_glyc':(0,0),
             'STEROLS_glyc':(0,0),
             'BIOMASS':(0,0),
             'PROTEINS':(0,0),
             'LIPIDS':(0,0),
             'STEROLS':(0,0),
             'BIOMASS_meoh':(0,1000),
             'PROTEINS_meoh':(0,1000),
             'LIPIDS_meoh':(0,1000),
             'STEROLS_meoh':(0,1000)}


# In[17]:


style= [dict(selector="caption", props=[("font-size", "140%"),
                                        ("font-weight", "bold"),
                                        ("color", 'white')])]


glumeoh=pd.DataFrame(envcond_meoh,index=['lb','ub']).T
glumeoh.style.set_caption("Methanol").set_table_styles(style)


# In[18]:


# Print the current objective
print("Current objective:")
print(model.objective.expression)

# Change to a different reaction
model.objective = "Ex_biomass"  # 
print("\nNew objective (using reaction ID):")
print(model.objective.expression)


# In[19]:


#pFBA for WT

from cobra.flux_analysis import pfba
import pandas as pd

# 1️⃣ Apply environmental conditions
for reaction_id, bounds in envcond_meoh.items():
    rxn = model.reactions.get_by_id(reaction_id)
    rxn.bounds = bounds  # tuple/list: (lower_bound, upper_bound)

# 2️⃣ Check if FBA is feasible
solution_fba = model.optimize()
if solution_fba.status != 'optimal':
    raise ValueError("FBA is infeasible under these conditions. Adjust bounds!")

vmax = solution_fba.objective_value  # optimal objective

# 3️⃣ Fix the objective at vmax before running pFBA
with model:
    # Fix the objective reaction at its optimal value
    # Get the objective reaction ID correctly from the model
    # Find the reaction(s) that have non-zero objective coefficients
    objective_rxns = [r.id for r in model.reactions if r.objective_coefficient != 0]
    
    # If there's at least one objective reaction, fix its bounds
    if objective_rxns:
        objective_rxn = objective_rxns[0]  # Take the first one if multiple
        model.reactions.get_by_id(objective_rxn).bounds = (vmax, vmax)
    else:
        # Alternative method if objective_coefficient approach doesn't work
        # This gets the reaction IDs from the model's objective directly
        objective_dict = model.objective.to_json()
        objective_rxn = list(objective_dict.keys())[0]
        model.reactions.get_by_id(objective_rxn).bounds = (vmax, vmax)
    
    # Run pFBA
    solution_pfba = pfba(model)

# 4️⃣ Extract fluxes (pandas Series)
fluxes = solution_pfba.fluxes

# 5️⃣ Save full fluxes to CSV
fluxes.to_csv("pfba_fluxes_meoh_das.csv")

# 6️⃣ Optional: Save fluxes with reaction name and subsystem
df_flux = fluxes.to_frame(name="flux")
df_flux["reaction_name"] = [model.reactions.get_by_id(r).name for r in df_flux.index]
df_flux["subsystem"] = [model.reactions.get_by_id(r).subsystem for r in df_flux.index]
df_flux.to_csv("pfba_fluxes_meoh_detailed_das.csv")

# 7️⃣ Optional: Save only active (non-zero) fluxes
active_fluxes = fluxes[fluxes.abs() > 1e-6]
active_fluxes.to_csv("pfba_active_fluxes_meoh_das.csv")

print("pFBA completed successfully! Fluxes saved to CSV.")


# In[20]:


#pFBA for RuMP, deletion of DAS reactions

from cobra.flux_analysis import pfba

genes_to_delete = ["PAS_chr3_0832", "PAS_chr3_0834"]

# Create a copy of the model to avoid permanent changes
model_copy = model.copy()

try:
    # Try the gene knockouts
    for gid in genes_to_delete:
        model_copy.genes.get_by_id(gid).knock_out()
    
    # Check if the model is still viable
    solution_pfba = pfba(model_copy)
    fluxes = solution_pfba.fluxes
    
    # Save full fluxes to CSV
    fluxes.to_csv("pfba_fluxes_meoh_rumpi_TKL_15.csv")
    
    # Save fluxes with reaction name and subsystem
    df_flux = fluxes.to_frame(name="flux")
    df_flux["reaction_name"] = [model_copy.reactions.get_by_id(r).name for r in df_flux.index]
    df_flux["subsystem"] = [model_copy.reactions.get_by_id(r).subsystem for r in df_flux.index]
    df_flux.to_csv("pfba_fluxes_meoh_detailed_rumpi_TKL_15.csv")
    
    # Save only active (non-zero) fluxes
    active_fluxes = fluxes[fluxes.abs() > 1e-6]
    active_fluxes.to_csv("pfba_active_fluxes_meoh_rumpi_TKL_15.csv")
    
    print("pFBA completed successfully! Fluxes saved to CSV.")
    
except Exception as e:
    print(f"Model became infeasible after gene knockouts: {e}")
    print("Consider checking if these genes are essential or if there are alternative pathways.")
    
    affected_reactions = []
    for gid in genes_to_delete:
        gene = model.genes.get_by_id(gid)
        affected_reactions.extend([r.id for r in gene.reactions])
    
    print(f"Reactions affected by these genes: {affected_reactions}")


# In[21]:


#ATP consumption. Use atp_x, atp_m, atp_c for localization
atp = model.metabolites.get_by_id("atp_c")  

atp_consuming_rxns = []
for rxn in model.reactions:
    if atp in rxn.metabolites:
        if rxn.metabolites[atp] < 0:  # ATP is consumed
            atp_consuming_rxns.append(rxn)

#ATP consumption per reaction: ATP usage=∣νrxn​∣×∣ATP stoichiometry∣
total_atp_consumption = 0.0
atp_breakdown = []

for rxn in atp_consuming_rxns:
    v = fluxes[rxn.id]
    coeff = rxn.metabolites[atp]  # negative
    atp_used = abs(v * coeff)
    
    total_atp_consumption += atp_used
    atp_breakdown.append((rxn.id, atp_used))

import pandas as pd

df_atp = pd.DataFrame(atp_breakdown, columns=["reaction", "ATP_consumption"])
df_atp = df_atp.sort_values("ATP_consumption", ascending=False)

print("Total ATP consumption:", total_atp_consumption)
df_atp.to_csv("atp_consumption_breakdown.csv", index=False)


# In[ ]:




