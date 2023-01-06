from django.contrib.auth.models import User
from django.shortcuts import redirect,render

def Coach_secure_Login(get_response):
   
    def middleware(request):
        name=request.session.get('user_dt')
        if User.objects.filter(is_superuser=False):
            return redirect('players_Login')

        response = get_response(request)
        return response

    return middleware

def student_secure(get_response):
   
    def middleware(request):
        name=request.session.get('user_dt')
        if User.is_superuser==True:
           return redirect('Students_details')


        response = get_response(request)
        return response

    return middleware
