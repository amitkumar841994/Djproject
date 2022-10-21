from django.urls import path
from .import views
urlpatterns=[

    path('Home',views.Home,name='Home'),
    path('Personal/<int:pid>',views.Personal,name='Personal'),
    path('Adddetails',views.Adddetails,name='Adddetails'),
    path('Userdata',views.Userdata,name='Userdata'),
    path('Professonal/<int:pid>',views.Professonal,name='Professonal')

]