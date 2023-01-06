from django.db import models
from django.contrib.auth.models import User
class website(models.Model):
    usage=models.IntegerField()
    username=models.ForeignKey(User,on_delete=models.PROTECT)


# Create your models here.
