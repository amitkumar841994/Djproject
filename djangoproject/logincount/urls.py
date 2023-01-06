from django.urls import path
from .import views
urlpatterns=[
    path('logincount',views.loginpage,name='logincount')

]