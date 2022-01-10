from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=150)
    total_lessons = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=150)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    date = models.DateField()
    
    def __str__(self):
        return self.name

