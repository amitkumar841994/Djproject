from django.urls import path
from.import views
urlpatterns=[
    path('home',views.index,name='Home'),
    path('Food',views.food,name='food'),
    path('Login',views.login,name='login'),
    path('update/<int:tid>',views.update_food,name='update'),
    path('delete/<int:tid>',views.delete_food,name='delete'),
    path('user',views.userdata,name='user'),
    path('store',views.store_api,name='store'),
    path('viewstore/<int:pid>',views.viewstore,name='viewstore'),
]