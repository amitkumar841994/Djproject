from django.urls import path,include
from .import views
urlpatterns=[
    path('Home',views.Home,name='Home'),
    path('Task_details',views.Task_details,name='Task_details'),
    path('task_status/<int:pid>',views.task_status,name='task_status'),
    path('task_delete/<int:pid>',views.task_delete,name='task_delete')

]
