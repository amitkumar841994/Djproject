from django.db import models
class Signup(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contact=models.IntegerField()
    user=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
# Create your models here.
