import os, glob, csv
import pandas as pd
import numpy as np

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.views import APIView
from Database.forms import GeneralInformationForm
from Database.models import NaturalProducts

# Create your views here.


class ServerViews(APIView):
    def post(self, request):
        form = GeneralInformationForm(request.POST)
        form_dict = {
            "form": form,
        }
        if form.is_valid():
            form = form.save()
            print(form)
            _ = form.common_name
            print("soy form ", _)
            result = (
                NaturalProducts.objects.all()
                .filter(common_name=_)
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
            print("result", result[0])
            ids = list(result[0].keys())
            search_values = list()
            for i in ids:
                search_values.append(result[0][i])
            print(search_values)
            print(type(ids), type(search_values))
            d = np.array([ids, search_values])
            d = np.transpose(d)
            data = pd.DataFrame(data=d)
            # columns = ["ID","Family","Specie-1","Specie-2","Specie-3","Specie-4","Specie-5","Common name","SMILES","ACT-1","ACT-2","ACT-3","ACT-4","ACT-5","ACT-6","ACT-7","Source","Autors"]
            # print(data.columns)
            data = data.to_html()
            return render(request, "search_table.html", context={"data": data})
        return render(request, "home.html", context=form_dict)

    def get(self, request):
        form = GeneralInformationForm(request.POST)
        form_dict = {
            "form": form,
        }
        return render(request, "home.html", context=form_dict)


class About(APIView):
    def get(self, request):
        return render(request, "about.html")

