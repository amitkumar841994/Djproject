from django.contrib import admin
from.models import User,website

class website_admin(admin.ModelAdmin):
    list_display=['usage','username']
admin.site.register(website,website_admin)

# Register your models here.
