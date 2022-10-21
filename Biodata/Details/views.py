from cgitb import html
from pickletools import read_uint1
from winreg import REG_QWORD
from django.shortcuts import redirect, render
from .models import UserDetails

def Home(request):
    userdt=UserDetails.objects.all()
    return render(request,'Index.html',{'userdata':userdt})
def Personal(request,pid):
    userdata=UserDetails.objects.get(id=pid)
    print(pid)

    return render(request,'Personal.html',{'usrdt':userdata})
def Professonal(request,pid):
     userdata=UserDetails.objects.get(id=pid)
     return render(request,'Professonal.html',{'usrdt':userdata})

def Adddetails(request):

    if request.method=='POST':
        userdt=UserDetails()
        userdt.FirstName=request.POST.get('FirstName')
        userdt.LastName=request.POST.get('LastName')
        userdt.FatherName=request.POST.get('FatherName')
        userdt.MotherName=request.POST.get('MotherName')
        userdt.Gender=request.POST.get('Gender')
        userdt.EmailId=request.POST.get('Email')
        userdt.Educations=request.POST.get('Educations')
        userdt.Experience=request.POST.get('Experience')
        userdt.Hobbies=request.POST.get('Hobbies')
        userdt.Skill=request.POST.get('Skill')
        userdt.Descripiton=request.POST.get('Descripiton')
        userdt.save()
    return render(request,'Adddetails.html')
  

def Userdata(request):
    
    userdt=UserDetails.objects.all()
    return render(request,'Userdata.html',{'userdata':userdt})
    
