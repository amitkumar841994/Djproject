from django.contrib import admin
from.models import Food
class Food_admin(admin.ModelAdmin):
    list_display=['Food_id','Food_name','Food_price','Food_cate']

admin.site.register(Food,Food_admin)

# Register your models here.
