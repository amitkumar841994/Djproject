from django.contrib import admin
from .models import Coach_register

class Coach_register_admin(admin.ModelAdmin):

        list_display=[

    'id','Firstname', 'Lastname','username','gender','Dob','Address','state','city','pincode','Coach_for','Experience','email','mobile'
    ]

admin.site.register(Coach_register,Coach_register_admin)
# Register your models here.
