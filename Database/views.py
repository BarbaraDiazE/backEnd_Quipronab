import os, glob, csv
import pandas as pd
import numpy as np

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.views import APIView
from Database.forms import GeneralInformationForm
from modules.search import get_common_name, get_family

# Create your views here.


class ServerViews(APIView):
    def post(self, request):
        form = GeneralInformationForm(request.POST)
        if form.is_valid():
            form = form.save()
            common_name = form.common_name
            family = form.family
            specie = form.specie
            print(common_name, family, specie)
            if common_name:
                data = get_common_name(common_name)
            elif family:
                data = get_family(family, specie)
            return render(request, "search_table.html", context={"data": data.to_html()})
        return render(request, "home.html", context={"form": form} )

    def get(self, request):
        form = GeneralInformationForm(request.POST)
        form_dict = {
            "form": form,
        }
        return render(request, "home.html", context=form_dict)


class About(APIView):
    def get(self, request):
        return render(request, "about.html")

