from django.db import models

class Task(models.Model):
    Task_name=models.CharField(max_length=100)
    Task_status=models.CharField(max_length=50,default='In-progress',editable=True)
# Create your models here.
