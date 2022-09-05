from django.db import models





class Person(models.Model):
    name = models.CharField(('name'), max_length=255, unique=True, help_text=("Name of the FAQ Topic"))
