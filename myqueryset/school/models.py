from django.db import models

class MyStudentModel(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField(unique=True,null=False)
    city=models.CharField(max_length=500)
    marks=models.IntegerField()
    passing_year=models.DateField()


    