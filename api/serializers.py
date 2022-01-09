from .models import Lesson, Module
from rest_framework import serializers


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'module', 'date']


class ModuleSerializer(serializers.HyperlinkedModelSerializer):
    lesson_set = LessonSerializer(many=True)
    class Meta:
        model = Module
        fields = ['id', 'name', 'lesson_set']