from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import HospitalSerializer
from .models import hospital
class HospitalsList(APIView):
    def get(self, request, pincode=None):
        if pincode==None:
            hospitals=hospital.objects.all()
            serializer=HospitalSerializer(hospitals, many=True)
            return Response(serializer.data)
        elif pincode:
            hospitals=hospital.objects.filter(pincode__exact=pincode)
            serializer=HospitalSerializer(hospitals, many=True)
            return Response(serializer.data)
        def get(request, state):
            hospitals=hospital.objects.filter(state__exact=state)
            serializer=HospitalSerializer(hospitals, many=True)
            return Response(serializer.data)

    def post(selfr):
        pass