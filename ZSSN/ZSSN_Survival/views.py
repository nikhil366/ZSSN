from functools import partial
from itertools import count
from optparse import Values
from django.shortcuts import render
from .models import Survivor
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import SerializersSurvivor
import math


class SurvivorView(viewsets.ViewSet):
    
    # POST API
    def create(self, request): 
        try:    
            data = request.data
            serializeData = {
                "name":data["name"],
                "age":data["age"],
                "gender":data["gender"],
                "longitude":data["location"]["longitude"],
                "latitude":data["location"]["latitude"],
                "is_infected":data["is_infected"]
            }
            serializer = SerializersSurvivor(data=serializeData)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"status": "error", "Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    # GET API
    def list(self, request):
        survivor = Survivor.objects.all()
        serializer = SerializersSurvivor(survivor, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    # PUT/Update API
    def update(self, request, pk = None):
        try: 
            id = pk
            updateSurvivor = Survivor.objects.get(pk=id)
            serializer = SerializersSurvivor(updateSurvivor, data = request.data, partial=True)
        
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success, Location Updated ","data":serializer.data})
        except Exception as e:
            return Response({"status": "error", "Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class SurvivorPercentage(viewsets.ViewSet):
    # GET API
    def list(self, request):
        
        infected = 0
        nonInfected = 0
        survivor = Survivor.objects.all()
        for s in survivor:
            if s.is_infected == "Infected":
                infected = infected+1
            elif s.is_infected == "Non-Infected":
                nonInfected = nonInfected+1

        infectedPer = math.trunc((infected/survivor.count()) * 100)
        nonInfectedPer = math.trunc((nonInfected/survivor.count()) * 100)

        return Response({"status": "success",
                         "data": {"infected%":infectedPer,
                                  "nonInfected%":nonInfectedPer }}, 
                         status=status.HTTP_200_OK)
    




