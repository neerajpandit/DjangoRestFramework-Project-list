from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=10)
    roll=serializers.CharField(max_length=10)
    city=serializers.CharField(max_length=10)

    def create(self,validate_data):
        return Student.objects.create(**validate_data)

