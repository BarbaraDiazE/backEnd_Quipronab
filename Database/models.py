import csv

from django.db import models
from django.db.utils import DataError

class NaturalProducts(models.Model):
    ID          = models.CharField(max_length=500, primary_key=True) 
    family      = models.CharField(max_length = 500, null = False)
    specie_1    = models.CharField( max_length = 500, null = False)
    specie_2    = models.CharField( max_length = 500, null = False)
    specie_3    = models.CharField( max_length = 500, null = False)
    specie_4    = models.CharField( max_length = 500, null = False)
    specie_5    = models.CharField( max_length = 500, null = False)
    common_name = models.CharField( max_length = 500, null = False)
    smiles      = models.CharField( max_length = 500, null = False)
    act_1       = models.CharField( max_length = 500, null = False)
    act_2       = models.CharField( max_length = 500, null = False)
    act_3       = models.CharField( max_length = 500, null = False)
    act_4       = models.CharField( max_length = 500, null = False)
    act_5       = models.CharField( max_length = 500, null = False)
    act_6       = models.CharField( max_length = 500, null = False)
    act_7       = models.CharField( max_length = 500, null = False)
    source      = models.CharField( max_length = 500, null = False)
    autors      = models.CharField( max_length = 500, null = False)

@classmethod
def populate(cls):
    data = csv.DictReader(open('QPN_2020.csv'))
    for row in data:
        try:
            cls.objects.create(
                                ID          = row['ID'],
                                family      = row['Family'], 
                                specie_1    = row['Specie-1'],
                                specie_2    = row['Specie-2'],
                                specie_3    = row['Specie-3'],
                                specie_4    = row['Specie-4'],
                                specie_5    = row['Specie-5'],
                                common_name = row['Common name'],
                                smiles      = row['SMILES'],
                                act_1       = row['ACT-1'],
                                act_2       = row['ACT-2'],
                                act_3       = row['ACT-3'],
                                act_4       = row['ACT-4'],
                                act_5       = row['ACT-5'],
                                act_6       = row['ACT-6'],
                                act_7       = row['ACT-7'],
                                source      = row['Source'],
                                autors      = row['Autors'],
                                        )
        except DataError as e:
                print(e)

@classmethod
def clean_table(cls):
    cls.objects.all().delete()
