from django import forms
from Database.models import GeneralInformation


class GeneralInformationForm(forms.ModelForm):
    class Meta:
        model = GeneralInformation
        fields = (
            "common_name",
            "family",
            "specie",
            "mw_low",
            "mw_high",
            "logp_low",
            "logp_high",
            "tpsa_low",
            "tpsa_high",
            "lipinsky_low",
            "lipinsky_high",
            "hba_low",
            "hba_high",
            "hbd_low",
            "hbd_high",
            "rb_low",
            "rb_high",
        )

