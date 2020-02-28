import csv

from django import forms
from django.db import models
from django.db.utils import DataError


class NaturalProducts(models.Model):
    ID = models.CharField(max_length=500, primary_key=True)
    family = models.CharField(max_length=500, null=False)
    specie_1 = models.CharField(max_length=500, null=False)
    specie_2 = models.CharField(max_length=500, null=False)
    specie_3 = models.CharField(max_length=500, null=False)
    specie_4 = models.CharField(max_length=500, null=False)
    specie_5 = models.CharField(max_length=500, null=False)
    common_name = models.CharField(max_length=500, null=False)
    smiles = models.CharField(max_length=500, null=False)
    act_1 = models.CharField(max_length=500, null=False)
    act_2 = models.CharField(max_length=500, null=False)
    act_3 = models.CharField(max_length=500, null=False)
    act_4 = models.CharField(max_length=500, null=False)
    act_5 = models.CharField(max_length=500, null=False)
    act_6 = models.CharField(max_length=500, null=False)
    act_7 = models.CharField(max_length=500, null=False)
    source = models.CharField(max_length=500, null=False)
    autors = models.CharField(max_length=500, null=False)


@classmethod
def clean_table(cls):
    cls.objects.all().delete()


class GeneralInformation(models.Model):
    common_name = models.CharField(
        max_length=500, verbose_name="common name", help_text="name", blank=True
    )
    family = models.CharField(
        max_length=500, verbose_name="family", help_text="family", blank=True
    )
    specie = models.CharField(
        max_length=500, verbose_name="specie", help_text="specie", blank=True
    )

