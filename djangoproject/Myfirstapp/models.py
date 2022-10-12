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
    


# Create your models here.
