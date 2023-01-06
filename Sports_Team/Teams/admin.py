from django.contrib import admin
from .models import Team_register

class Team_register_admin(admin.ModelAdmin):
    list_display=['id','Firstname', 'Lastname','username','gender','Dob','Address','state','city','pincode','sport','disability','height','email','mobile']
# Register your models here.
admin.site.register(Team_register,Team_register_admin)