from django.urls import path
from .import views
urlpatterns=[
   path('Player_home',views.Player_home,name='Player_home'),
    path('player_register',views.Team_registrations,name='player_register'),
    path('players_Login',views.Team_Login,name='players_Login'),
    path('Player_logout',views.Player_logout,name='Player_logout'),
    path('Player_Profile',views.Player_Profile,name='Player_Profile')

] 