from django.contrib import admin
from .models import MyStudentModel

@admin.register(MyStudentModel)
class MyStudentModelAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city','marks','passing_year']
    
