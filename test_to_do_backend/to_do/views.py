from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets

from .models import Lists, Tasks
from .serializer import ListsSerializer, TasksSerializer


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TasksSerializer
    
    def get_queryset(self):
        return Tasks.objects.filter(is_active = True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

class ListViewSet(viewsets.ModelViewSet):
    serializer_class = ListsSerializer
    
    def get_queryset(self):
        return Lists.objects.filter(is_active = True)
    
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

        tasks = Tasks.objects.filter(list=instance) #va a traer todas las tareas que pertenescan a esa lista
        for task in tasks:
            task.is_active = False
            task.save()

