from django.contrib import admin
from.models import Task

class Task_admin(admin.ModelAdmin):
    list_display=['Task_name','Task_status']

admin.site.register(Task,Task_admin)

# Register your models here.
