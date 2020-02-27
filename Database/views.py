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
            return HttpResponse(f'{form}')
            #return redirect(f"/csv/{filename}/")
        return render(request, "home.html", context=form_dict)
    def get(self, request):
        return render(request, "home.html")

class About(APIView):
    def get(self, request):
        return render(request, "about.html")

