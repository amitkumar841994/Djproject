from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Middleware.auth import Coach_secure_Login,student_secure
from .models import Coach_register
from Teams.models import Team_register
@Coach_secure_Login
def Coach_home(request):
    return render(request,'Coach_home.html')

@Coach_secure_Login
def Coach_Login(request):
    msg=''
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            request.session['user_dt']=username
            print(request.session.get('user_dt'))
            return redirect('Coach_home') 

        else:
            msg='User or Password does not match'

    return render(request,'Coach_Login.html',{'msg':msg})

def Coach_logout(request):
    logout(request)
    return redirect('Coach_home')


def Coach_registrations(request):
    msg=''
    if request.method=='POST':
        firstname=request.POST.get('fname')
        lastnane=request.POST.get('lname')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        gender=request.POST.get('gender')
        Dob=request.POST.get('Dob')
        address=request.POST.get('address')
        state=request.POST.get('state')
        city=request.POST.get('city')
        pincode=request.POST.get('pincode')
        Coach_for=request.POST.get('Coach_for')
        experience=request.POST.get('experience')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        user_chk=User.objects.filter(username=username)
        if len(user_chk)==0:
            if password1==password2:
                user=User.objects.create_superuser(username=username,email=email,password=password1,first_name=firstname,last_name=lastnane)
                user.save()
            # print(user)
                coach_dt=Coach_register.objects.create(
                    Firstname=firstname,
                    Lastname=lastnane,
                    gender=gender,
                    Dob=Dob,
                    Address=address,
                    state=state,
                    city=city,
                    pincode=pincode,
                    Coach_for=Coach_for,
                    Experience=experience,
                    email=email,
                    mobile=mobile,
                )
                coach_dt.save()
            else:
                msg="Password does not match"
        else:
            msg="User already exists"
        
        
       
    return render(request,'Coach_registrations.html',{'msg':msg})
@login_required
def Coach_Dashboard(request):
    user_dt=request.session.get('user_dt')
    coach_dt=Coach_register.objects.all()
    return render(request,'Coach_Dashboard.html',{'data':coach_dt,'user_dt':user_dt})

@student_secure
def Students_details(request):
    user_dt=request.session.get('user_dt')
    abc=User.objects.filter(username=user_dt)
    print(abc)
    # Students_dt=Team_register.objects.all()
    #print(user_dt)
    Students_dt=Team_register.objects.all()
    
    current_user=request.user
    print(current_user)
    
        
    return render(request,'Students_details.html',{'Students_dt':Students_dt})

    # Create your views here.
