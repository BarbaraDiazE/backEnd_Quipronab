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
    mw = models.FloatField(null=False)
    hba = models.FloatField(null=False)
    hbd = models.FloatField(null=False)
    tpsa = models.FloatField(null=False)
    rb = models.FloatField(null=False)
    logp = models.FloatField(null=False)
    fsp3 = models.FloatField(null=False)
    lipinsky = models.FloatField(max_length=100)


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
        max_length=500, verbose_name="specie", help_text="specie", blank=True,
    )
    mw_lt = models.FloatField(
        verbose_name="MW", help_text="lt MW", blank=True, null=True
    )
    mw_gt = models.FloatField(
        verbose_name="MW", help_text="gt MW", blank=True, null=True
    )
    hba_lt = models.FloatField(
        verbose_name="HBA", help_text="lt HBA", blank=True, null=True
    )
    hba_gt = models.FloatField(
        verbose_name="HBA", help_text="gt HBA", blank=True, null=True
    )
    hbd_lt = models.FloatField(
        verbose_name="HBD", help_text="lt HBD", blank=True, null=True
    )
    hbd_gt = models.FloatField(
        verbose_name="HBD", help_text="gt HBD", blank=True, null=True
    )
    tpsa_lt = models.FloatField(
        verbose_name="TPSA", help_text="lt TPSA", blank=True, null=True
    )
    tpsa_gt = models.FloatField(
        verbose_name="TPSA", help_text="gt TPSA", blank=True, null=True
    )
    rb_lt = models.FloatField(
        verbose_name="RB", help_text="lt RB", blank=True, null=True
    )
    rb_gt = models.FloatField(
        verbose_name="RB", help_text="gt RB", blank=True, null=True
    )
    logp_lt = models.FloatField(
        verbose_name="LogP", help_text="lt  LogP", blank=True, null=True
    )
    logp_gt = models.FloatField(
        verbose_name="LogP", help_text="gt LogP", blank=True, null=True
    )
    fsp3_lt = models.FloatField(
        verbose_name="Fraction Csp3",
        help_text="lt Fraction Csp3",
        blank=True,
        null=True,
    )
    fsp3_gt = models.FloatField(
        verbose_name="Fraction Csp3",
        help_text="gt Fraction Csp3",
        blank=True,
        null=True,
    )
    lipinsky_lt = models.FloatField(
        verbose_name="Lipinsky", help_text="lt Lipinsky", blank=True, null=True
    )
    lipinsky_gt = models.FloatField(
        verbose_name="Lipinsky", help_text="gt Lipinsky", blank=True, null=True
    )
    smiles = models.CharField(
        verbose_name="smiles", max_length=100, blank=True, null=True
    )

