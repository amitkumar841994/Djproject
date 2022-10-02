from django.urls import path
from.import views
urlpatterns=[
    path('home',views.index),
    path('Food',views.food,name='food'),
    path('Login',views.login,name='login')
]