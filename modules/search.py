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

def get_chemical_information(form):
    result = NaturalProducts.objects.exclude(mw__lt=form.mw_lt).exclude(mw__gt=form.mw_gt)
    result = result.exclude(hba__lt=form.hba_lt).exclude(hba__gt=form.hba_gt)
    #hbd
    result = result.exclude(hbd__lt=form.hba_lt).exclude(hbd__gt=form.hba_gt)
    #tpsa
    result = result.exclude(tpsa__lt=form.tpsa_lt).exclude(tpsa__gt=form.tpsa_gt)
    #rb
    result = result.exclude(rb__lt=form.rb_lt).exclude(rb__gt=form.rb_gt)
    #logp
    result = result.exclude(logp__lt=form.logp_lt).exclude(logp__gt=form.logp_gt)
    #fsp3
    result = result.exclude(fsp3__lt=form.fsp3_lt).exclude(fsp3__gt=form.fsp3_gt)
    #lipinsky
    result = result.exclude(lipinsky__lt=form.lipinsky_lt).exclude(lipinsky__gt=form.lipinsky_gt)
    result = result.values("ID", "family", "specie_1", "mw", "hba", "hbd", "tpsa", "rb", "logp", "fsp3", "lipinsky")
    search_values = list(map(lambda x: result[x].values(), range(len(result))))
    data = pd.DataFrame(data=search_values, columns = ["ID", "Family", "Specie_1", "mw", "hba", "hbd", "tpsa", "rb", "logp", "fsp3", "lipinsky" ]).set_index("ID")
    return data
    