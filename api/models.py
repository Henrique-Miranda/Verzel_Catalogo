from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=150)

class Lesson(models.Model):
    name = models.CharField(max_length=150)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    date = models.DateField()

