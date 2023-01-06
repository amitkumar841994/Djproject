from django.db import models
from django.contrib.auth.models import User

class Team_register(models.Model):
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    gender=models.CharField(max_length=50)
    Dob=models.DateField()
    Address=models.CharField(max_length=300)
    state=models.CharField(max_length=60)
    city=models.CharField(max_length=100)
    pincode=models.IntegerField()
    sport=models.CharField(max_length=100)
    disability=models.CharField(max_length=30)
    height=models.FloatField()
    email=models.CharField(max_length=100)
    mobile=models.IntegerField()
    username=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    # S
# Create your models here.
