from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from task.models import Record
from task.serializers import RecordSerializer


class RecordList(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordCreate(generics.CreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
