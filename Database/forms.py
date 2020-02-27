from django import forms
from Database.models import GeneralInformation

class GeneralInformationForm(forms.ModelForm):
    class Meta:
        model = GeneralInformation
        fields = ("common_name",)