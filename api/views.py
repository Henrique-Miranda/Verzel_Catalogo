from django.shortcuts import render
from .models import Lesson, Module
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .serializers import LessonSerializer, ModuleSerializer

# Reference https://www.devaria.com.br/conteudo-das-aulas
""" Authentication https://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme
and https://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme"""

class LessonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Lesson.objects.all().order_by('name')
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

class ModuleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Module.objects.all().order_by('name')
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]