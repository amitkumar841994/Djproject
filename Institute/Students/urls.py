from django.urls import URLPattern, path
from .import views
urlpatterns=[
   
   path('Home',views.home,name='Home'),
   path('Login',views.Login,name='Login'),
   path('Signup',views.Signup,name='Signup')
    
]
