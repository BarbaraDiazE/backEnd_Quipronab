from django import forms
from Database.models import GeneralInformation


class GeneralInformationForm(forms.ModelForm):
    class Meta:
        model = GeneralInformation
        fields = ("common_name", "family", "specie", "MW_low", "MW_high", "LogP_low", "LogP_high", "TPSA_low", 
                    "TPSA_high",  
                    "Lipinsky_low",  
                    "Lipinsky_high",  
                    "HBA_low", 
                    "HBA_high", 
                    "HBD_low", 
                    "HBD_high", 
                    "RB_low", 
                    "RB_high" 
                        )

