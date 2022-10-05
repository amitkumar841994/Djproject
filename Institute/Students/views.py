from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,'index.html')

def Signup(request):
    return render(request,'Signup.html')

def Login(request):
    return render(request,'Login.html')


# Create your views here.
