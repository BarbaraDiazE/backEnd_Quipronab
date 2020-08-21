import os
import glob
import csv
import pandas as pd
import numpy as np

# import numpy as np

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView, View
from Database.forms import GeneralInformationForm, SmilesModelForm
from modules.search import *

from django.views.generic import DetailView

from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view

# Create your views here.


class ServerViews(APIView):
    def post(self, request):
        form = GeneralInformationForm(request.POST)
        if form.is_valid():
            form = form.save()
            print("form")
            print(form)
            common_name = form.common_name
            family = form.family
            specie = form.specie
            mw_lt = form.mw_lt
            smiles = form.smiles
            print(smiles)
            if common_name:
                data = get_common_name(common_name)
            elif family:
                data = get_family(family, specie)
            elif mw_lt:
                print("mw", mw_lt)
                data = get_chemical_information(form)
            elif smiles:
                data = get_common_name("engeletina")

            return render(
                request, "search_table.html", context={"data": data.to_html()}
            )
        return render(request, "home.html", context={"form": form})

    def get(self, request):
        form = GeneralInformationForm(request.POST)
        form_dict = {
            "form": form,
        }
        return render(request, "home.html", context=form_dict)


class About(APIView):
    def get(self, request):
        return render(request, "about.html")


# class Drawer(APIView):
#     def post(self, request):
#         smiles = request.POST.get("smiles")
#         # s = request.POST.get("smiles")
#         print("smiles:", smiles)
#         if smiles != None:
#             # print("SMILES: ", smiles)
#             # data = get_similar_compounds(smiles)
#             # return render(
#             #     request, "search_table.html", context={"data": data.to_html()}
#             # )
#             #
#             return HttpResponse("no estoy fallando")
#         else:
#             return HttpResponse("estoy fallando")
#         # print(type(smiles))
#         # return render(request, "JSME.html")

#     def get(self, request):
#         return render(request, "JSME.html")


def drawer(request):
    if request.POST:
        print("post request")  # return HttpResponse("post homepage")
        # return render(request, "homepage", context)
        return HttpResponse("post request")
    else:
        print("homepage request")
        return render(request, "JSME.html")


def hola(request):
    if request.POST:
        smiles = request.POST["smiles"]
        return render(request, "JSME.html")


def ajaxsave(request):
    smiles = request.POST["smiles"]
    print(smiles)
    print("soy la funcion ajax")
    return JsonResponse({"smiles": smiles})
