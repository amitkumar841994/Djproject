from django.db import models

class Food(models.Model):
    Food_id=models.IntegerField()
    Food_name=models.CharField(max_length=50)
    Food_price=models.IntegerField()
    Food_cate=models.CharField(max_length=50)


# Create your models here.
