from django.urls import path
from.import views
urlpatterns=[
    path('home',views.index,name='Home'),
    path('Food',views.food,name='food'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('update/<int:tid>',views.update_food,name='update'),
    path('delete/<int:tid>',views.delete_food,name='delete'),
    path('user',views.userdata,name='user'),
    path('store',views.store_api,name='store'),
    path('viewstore/<int:pid>',views.viewstore,name='viewstore'),
    path('store_search/<cat>',views.store_search,name='store_search'),
    path('setsession',views.setsession,name='setsession'),
    path('getsession',views.getsession,name='getsession'),
    path('logoutpage',views.logoutpage,name="logoutpage"),
    path('userregister',views.userregister,name='userregister'),
    path('userdel/<int:pid>',views.userdel,name='userdel'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('jobpage',views.jobpage,name='jobpage'),
    path('jobdel/<int:pid>',views.deletejob,name='jobdel'),
    path('updatejob/<int:pid>',views.updatejob,name='updatejob'),
    path('test',views.test_dt,name='test')
]