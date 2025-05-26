from django.db import models

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=100)
    rollno=models.IntegerField()
    marks=models.IntegerField()
    college=models.CharField(max_length=100)
    gf=models.CharField(max_length=60)
    bf=models.CharField(max_length=60)
    
    
    
