import csv, os
from django.core.management.base import BaseCommand
from Database.models import NaturalProducts

class Command(BaseCommand):
    help = "Populate Database process"

    def handle(self, *args, **options): 
        #NaturalProducts.clean_table()
        data = csv.DictReader(open('QPN_2020.csv'))
        for row in data:
            try:
                NaturalProducts.objects.create(
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
                self.stdout.write('Table populated')
            except KeyError as e:
                    print(e)

