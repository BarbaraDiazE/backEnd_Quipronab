from django import forms
from Database.models import GeneralInformation, SmilesModel


class GeneralInformationForm(forms.ModelForm):
    class Meta:
        model = GeneralInformation
        fields = (
            "common_name",
            "family",
            "specie",
            "mw_lt",
            "mw_gt",
            "hba_lt",
            "hba_gt",
            "hbd_lt",
            "hbd_gt",
            "tpsa_lt",
            "tpsa_gt",
            "rb_lt",
            "rb_gt",
            "logp_lt",
            "logp_gt",
            "fsp3_lt",
            "fsp3_gt",
            "lipinsky_lt",
            "lipinsky_gt",
            "smiles",
        )


class SmilesModelForm(forms.ModelForm):
    class Meta:
        model = SmilesModel
        fields = ["smiles"]
        # widgets = {
        # 'smiles': forms.TextInput(attrs = {'class':'form-control',}),
