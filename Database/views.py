from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.views import APIView

import os, glob, csv

# Create your views here.


class ServerViews(APIView):
    def get(self, request):
        return render(request, "home.html")

class About(APIView):
    def get(self, request):
        return render(request, "about.html")

