from turtle import mode
from django.db import models

class UserDetails(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    FatherName = models.CharField(max_length=50)
    MotherName = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)
    EmailId = models.EmailField()
    Educations = models.CharField(max_length=250)
    Experience = models.CharField(max_length=300)
    Hobbies = models.CharField(max_length=100)
    Skill = models.CharField(max_length=100)
    Descripiton = models.CharField(max_length=500)