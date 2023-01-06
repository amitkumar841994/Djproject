from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate,login,logout


def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        users=authenticate(username=username,password=password)
        if users is not None:
            login(request,users)
            request.session['userdata']=username
            userget=request.session.get('userdata')
            return HttpResponse('Loggin')
        else:
            HttpResponse('not loggedin')

    return render(request,'loginpage.html')
