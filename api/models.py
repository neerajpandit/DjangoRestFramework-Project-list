from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=10,null=True)
    roll=models.CharField(max_length=10,null=True)
    city=models.CharField(max_length=10,null=True)