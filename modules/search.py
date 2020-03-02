"""
Manage search Queries
"""
import os

import pandas as pd 
import numpy as np

from Database.forms import GeneralInformationForm
from Database.models import NaturalProducts
from modules.variable_names import index_columns

def get_common_name(common_name):
    result = (
                NaturalProducts.objects.all()
                .filter(common_name=common_name)
                .values(
                    "ID",
                    "family",
                    "specie_1",
                    "specie_2",
                    "specie_3",
                    "specie_4",
                    "specie_5",
                    "common_name",
                    "smiles",
                    "act_1",
                    "act_2",
                    "act_3",
                    "act_4",
                    "act_5",
                    "act_6",
                    "act_7",
                    "source",
                    "autors",
                )
            )
    ids = list(result[0].keys())
    search_values = list()
    for i in ids:
        search_values.append(result[0][i])
    d = np.array([search_values])
    d = np.transpose(d)
    data = pd.DataFrame(data=d, index=index_columns, columns=[" "])
    return data

def get_family(family, specie):
    if len(specie)>0:
        result = (
            NaturalProducts.objects.all().filter(family=family, specie_1 = specie).values( "ID",
                "family",
                "specie_1", 
                "specie_2",
                 "common_name",
                "smiles",
                "act_1",
                "act_2",
                "act_3",
                "source",
                "autors"))
    else:
        result = (
            NaturalProducts.objects.all()
            .filter(family=family)
            .values(
                "ID",
                "family",
                "specie_1",
                "specie_2",
                "common_name",
                "smiles",
                "act_1",
                "act_2",
                "act_3",
                "source",
                "autors",
            )
        )
    search_values = list(map(lambda x: result[x].values(), range(len(result))))
    print(search_values)
    data = pd.DataFrame(data=search_values, columns = [
            "ID",
            "Family",
            "Specie_1",
            "Specie_2",
            "Common name",
            "SMILES",
            "act 1",
            "act 2",
            "act 3",
            "Source",
            "Autors"]).set_index("ID")
    return data