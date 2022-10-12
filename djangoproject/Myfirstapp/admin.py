from django.contrib import admin
from.models import Food,User
class Food_admin(admin.ModelAdmin):
    list_display=['Food_id','Food_name','Food_price','Food_cate']

admin.site.register(Food,Food_admin)

class User_admin(admin.ModelAdmin):
    list_display=['User_id','User_name','User_email','User_mobile']

admin.site.register(User,User_admin)

# Register your models here.
