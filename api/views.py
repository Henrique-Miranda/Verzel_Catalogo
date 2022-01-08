from django.shortcuts import render
from .models import Lesson, Module
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import LessonSerializer, ModuleSerializer

#https://www.devaria.com.br/conteudo-das-aulas

class LessonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Lesson.objects.all().order_by('name')
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

class ModuleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Module.objects.all().order_by('name')
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]