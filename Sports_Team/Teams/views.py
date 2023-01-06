from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Team_register
from Middleware.auth import Coach_secure_Login

def Player_home(request):
    return render(request,'Player_home.html')

def Team_registrations(request):
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
        sport=request.POST.get('sport')
        disability=request.POST.get('disability')
        height=request.POST.get('height')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        user=User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastnane)
        user.save()
        uname=User.objects.filter(username=username)
        player_dt=Team_register.objects.create(
            Firstname=firstname,
            Lastname=lastnane,
            gender=gender,
            Dob=Dob,
            Address=address,
            state=state,
            city=city,
            pincode=pincode,
            sport=sport,
            disability=disability,
            height=height,
            email=email,
            mobile=mobile, 
        )
        Team_register.username=uname
        player_dt.save()

    return render(request,'Players_registrations.html')


def Team_Login(request):
    msg=""
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            request.session['user_dt']=username
            return redirect('Player_home')
        else:
            msg='Username or Password does not match'
    return render(request,'Players_Login.html',{'msg':msg})

def Player_logout(request):
    logout(request)
    return redirect('Player_home')
@login_required
def Player_Profile(request):
    player_dt=Team_register.objects.all()

    return render(request ,'Player_Profile.html',{'data':player_dt})

# Create your views here.
