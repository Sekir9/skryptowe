import sqlite3
import requests
import json
import datetime
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

output = "Wrong value"

def getRates(fromDate, toDate):
    rates = {}
    conn = sqlite3.connect('Cortland.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT Id,Date, USDsales, PLNsales
                                     FROM AllSales''')

    start = datetime.datetime.strptime(fromDate, "%Y-%m-%d")
    end = datetime.datetime.strptime(toDate, "%Y-%m-%d")
   
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days + 1)]   
    datesWithFormat = []
    rates = []

    for rangeDates in date_generated:
        rangeDates = rangeDates.date()
        datesWithFormat.append(str(rangeDates))
        

    for elem in cursor:
        if elem[1] in datesWithFormat:
            temp = {
                "Date": elem[1],
                "USD Sales": elem[2],
                "PLN Sales": elem[3]
            }
            rates.append(temp)
    return rates

class MultiSales(APIView):  

    def get(self, request, fromDate= '2019-05-15', toDate = "2019-05-20"):

        data = getRates(fromDate,toDate)
        if data == None or data == []:
            data = {
                output: 'Wrong link'
            } 

        return Response(data)