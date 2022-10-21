from distutils.command.upload import upload
from unicodedata import category
from django.db import models

class Food(models.Model):
    Food_id=models.IntegerField()
    Food_name=models.CharField(max_length=50)
    Food_price=models.IntegerField()
    Food_cate=models.CharField(max_length=50)

class User(models.Model):
    
        User_id = models.IntegerField()
        User_name = models.CharField(max_length=50)
        User_email =models.CharField(max_length=50)
        User_mobile = models.IntegerField()

class Store(models.Model):
    title=models.CharField(max_length=50)
    descriptions=models.CharField(max_length=50)
    img=models.ImageField(upload_to="str_image")
    price=models.IntegerField()
    category=models.CharField(max_length=50)
    


# Create your models here.
