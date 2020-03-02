import rdkit
from rdkit import Chem
from rdkit.Chem import Descriptors, MolToSmiles
import os
import numpy as np 
import pandas as pd 

def compute_descriptors(smiles):

    smiles = list(map(lambda x: Chem.MolFromSmiles(x), smiles))
    CanonicalSmiles = list(map(lambda x: Chem.MolToSmiles(x), smiles))
    HBA = list(map(lambda x: Descriptors.NumHAcceptors(x), smiles))
    HBD = list(map(lambda x:Descriptors.NumHDonors(x), smiles))
    RB = list(map(lambda x: Descriptors.NumRotatableBonds(x), smiles)) 
    LOGP =  list(map(lambda x: Descriptors.MolLogP(x), smiles))
    TPSA =  list(map(lambda x: Descriptors.TPSA(x), smiles))
    MW = list(map(lambda x: Descriptors.MolWt(x), smiles))
    
    return CanonicalSmiles, HBA, HBD, RB, LOGP, TPSA, MW

data = pd.read_csv("/home/barbara/Documents/DIFACQUIM/backEnd_Quipronab/QPN_2020.csv")
smiles = data.SMILES.tolist()
print(smiles[:5])