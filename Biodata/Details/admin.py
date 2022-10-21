from django.contrib import admin
from .models import UserDetails

class UserDetails_admin(admin.ModelAdmin):
    list_display=['FirstName','LastName','FatherName','MotherName','Gender','EmailId','Educations','Experience','Hobbies','Skill','Descripiton']

admin.site.register(UserDetails,UserDetails_admin)

# Register your models here.
