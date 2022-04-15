from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarDetailSerializer, CarsListSerializer
from cars.models import Car
from cars.permissions import isOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer

class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()
    permissions_classes = (IsAuthenticated,)

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permissions_classes = (isOwnerOrReadOnly,)