from django.contrib import admin
from .views import Lesson, Module

admin.site.register(Lesson)
admin.site.register(Module)