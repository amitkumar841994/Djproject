from urllib import response
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User

def gaurd_middle(get_response):

    def middleware(request):
        name=request.session.get('userinfo')
        current_user=request.user
        if name is not None:
              return redirect('store')
        else:
              redirect('loginpage')

        response=get_response(request)
        return response
    return middleware
 