import sqlite3
import requests
import json
import os
import datetime
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from django.template import Context, loader




def index(request):
    #template = loader.get_template("MainPage.html")
    #return HttpResponse(template.render())
    return render(request, 'index.html')

def second(request):
    #template = loader.get_template("MainPage.html")
    #return HttpResponse(template.render())
    return render(request, 'secondView.html')
