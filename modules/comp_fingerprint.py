import numpy as np

import rdkit
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem, MACCSkeys
from rdkit.Chem.Fingerprints import FingerprintMols
from statistics import median, stdev


def maccskeys_fp(smiles_from_db):
    # ms = [Chem.MolFromSmiles(i) for i in smiles_from_db]
    ms = list()
    cleaned_smiles = list()
    for i in smiles_from_db:
        _ = Chem.MolFromSmiles(i)
        if _:
            ms.append(_)
            cleaned_smiles.append(i)
        else:
            continue
    fp_list = [MACCSkeys.GenMACCSKeys(x) for x in ms]
    # print(len(smiles_from_db), len(fp_list))
    return fp_list, cleaned_smiles


def target_mol_fp_representation(smiles):
    _ = Chem.MolFromSmiles(smiles)
    fp_target = MACCSkeys.GenMACCSKeys(_)
    return fp_target


def get_similarity(fp_target, fp_list):
    sim = np.around([DataStructs.TanimotoSimilarity(fp_target, i) for i in fp_list], 2)
    return sim


def get_similar_comp(sim, cleaned_smiles):
    _ = median(sim) + 2 * (stdev(sim))
    cota = np.around(_, 3)
    similar_compounds_idx = list()
    similar_compounds = list()
    for i in range(len(sim)):
        if sim[i] >= cota:
            similar_compounds_idx.append(i)
        else:
            continue
    for i in similar_compounds_idx:
        similar_compounds.append(cleaned_smiles[i])
    # similar_compounds = list(lambda parameter_list: expression)
    return similar_compounds
