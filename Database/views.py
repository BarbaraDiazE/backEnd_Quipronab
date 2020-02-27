import os, glob, csv

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.views import APIView
from Database.forms import GeneralInformationForm

# Create your views here.


class ServerViews(APIView):
    def post(self, request):
        form = GeneralInformationForm(request.POST)
        form_dict = {
            "form": form,
        }
        if form.is_valid():
            form = form.save()
            print(form.common_name)
            return HttpResponse("holi")
            #return redirect(f"/csv/{filename}/")
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

