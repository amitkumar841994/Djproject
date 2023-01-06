from django.urls import path
from .import views
urlpatterns=[
    path('Coach_home',views.Coach_home,name='Coach_home'),
    path('Coach_Login/',views.Coach_Login,name='Coach_Login'),
    path('Coach_logout',views.Coach_logout,name='Coach_logout'),
    path('Coach_register/',views.Coach_registrations,name='coach_register'),
    path('Coach_Dashboard/',views.Coach_Dashboard,name='Coach_Dshboard'),
    path('Students_details/',views.Students_details,name='Students_details'),


]