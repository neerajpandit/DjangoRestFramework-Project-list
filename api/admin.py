from django.contrib import admin

# Register your models here.
from .models import Student
admin.site.register(Student)
list_display=['id','name','roll','city']