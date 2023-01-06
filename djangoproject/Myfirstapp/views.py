from ast import Is, Not
from cgitb import html
from itertools import product
from math import prod
from pickle import NONE
import re
from unicodedata import category, name
from django.shortcuts import redirect, render,HttpResponse
import requests
from .models import Food,Store,User,Job,test
from .forms import Foodform, UserForm,Jobform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Myfirstapp.middleware.auth import gaurd_middle

def index(request):
     return render(request,'index.html')


def loginpage(request):
     if request.method=='POST':
          username=request.POST.get('username')
          password=request.POST.get('password')
          user=authenticate(username=username,password=password)
          print(user) 
          if user is not None:
               login(request,user)
               request.session['userinfo']=username 
               return redirect('food') 
          else:
               print(user)
               return redirect('loginpage')         
     return render(request,'Login.html')    

def logoutpage(request):
     logout(request)
     return redirect('loginpage') 
@gaurd_middle
def food(request):
     if request.method=='POST':
          food_data=Food()
          food_data.Food_id=request.POST.get('FoodID')
          food_data.Food_name=request.POST.get('Foodname')
          food_data.Food_price=request.POST.get('Foodprice')
          food_data.Food_cate=request.POST.get('Foodcat')
          name=request.POST.get('search')
          t=Food.objects.filter(Food_name=name,)# filter not working here
          food_data.save()
          # return render(request,'Food.html',{'food_dt':t})
     else:       
          food_data=Food.objects.all()
     return render(request,'Food.html',{'food_dt':food_data})

def foodsearch(request,cate):
     foser=Food.objects.filter(Food_cate=cate)
     if request.method=='POST':
          foser1=request.POST.get('search')
     return render(request,'Food.html',{'foser2':foser})


def update_food(request,tid):
     food=Food.objects.get(id=tid)
     print("update is working")
     form1=Foodform(instance=food)
     if request.method=='POST':
          form=Foodform(request.POST,instance=food)
          if form.is_valid():
               form.save()
     return render(request,'updatefood.html',{'fd_dt':form1})
     

def delete_food(request,tid):
     food_data=Food.objects.get(id=tid)
     food_data.delete()
     return redirect('food')

def userdata(request):
     form=UserForm()
     forms=UserForm(request.POST)
     if forms.is_valid():
          forms.save()
     return render(request,'userdata.html',{'dt':form})
@gaurd_middle
def store_api(request):
     # data=requests.get('https://fakestoreapi.com/products/')
    # apidata=data.json()
     product=Store.objects.all()
     # for i in range(len(apidata)):
     #      print(i)
     #      product=Store()
     #      product.title=apidata[i]['title']
     #      product.descriptions=apidata[1]['description']
     #      product.img=apidata[i]['image']
     #      product.price=apidata[i]['price']
     #      product.category=apidata[i]['category']
     #      product.save()

     return render(request,'productdata.html',{'str_data':product})

def store_search(request,cat):
     searched1=Store.objects.filter(category=cat)
     return render(request,'productdata.html',{'str_data':searched1})

def viewstore(request,pid):
     viewdata=Store.objects.get(id=pid)
     recent_products= None
     if 'viewed' in request.session:
          if pid in request.session['viewed']:
               request.session['viewed'].remove(pid)

          products=Store.objects.filter(pk__in=request.session['viewed'])
          print(products)
          product1=request.session['viewed'].insert(0,pid)
         
     else:
          request.session['viewed']=[pid]
     request.session.modified=True

     return render(request,'Viewstore.html',{'dt':viewdata,'dt1':products})

def setsession(request):
     request.session['test']='Amit'
     return HttpResponse("Session set")

def getsession(request):
     print(request.session.get('test'))

     return HttpResponse("Session set")
def userregister(request):
     msg=''
     userdt=User.objects.all()
     if request.method=='POST':
          username=request.POST.get('username')
          pwd1=request.POST.get('pwd1')
          pwd2=request.POST.get('pwd2')
          fname=request.POST.get('fname')
          lname=request.POST.get('lname')
          usern=User.objects.filter(username=username)
          print(usern)
          if len(usern)==0:
               if pwd1==pwd2:
                    users=User.objects.create_user(username=username,password=pwd1,first_name=fname,last_name=lname)
                    users.save()
                    msg=''
               else:
                    msg='Password does not match'
          else:
               msg='User already exist'
     return render(request,'userregister.html',{'msg1':msg,'userdt1':userdt})

def userdel(request,pid):
     userdel=User.objects.get(id=pid)
     userdel.delete()
     return redirect('userregister')


def changepassword(request):
     msg=''
     if request.method=='POST':
          username=request.POST.get('username')
          pwd1=request.POST.get('pwd1')
          pwd2=request.POST.get('pwd2')
          usern=User.objects.get(username=username)
          print(usern)
          if username in usern:
               if pwd1==pwd2:
                    usern.set_password(pwd1)
                    usern.save()
                    msg=''
               else:
                    msg='Password does not match'
          else:
               msg='User not exit'
     return render(request,'changepassword.html',{'msg1':msg})

def jobpage(request):
     jforms=Jobform(request.POST)
     if jforms.is_valid():
          jforms.save()
     jobdt=Job.objects.all()
     print(jobdt)

     return render(request, 'jobpage.html',{'jf':jforms,'jdt':jobdt})

def deletejob(request,pid):
     jobdel=Job.objects.get(id=pid)
     jobdel.delete()
     return redirect('jobpage')

def updatejob(request,pid):
     jobup=Job.objects.get(id=pid)
     jobfrm=Jobform(instance=jobup)
     if request.method=='POST':
          jobfrm1=Jobform(request.POST,instance=jobup)
          if jobfrm1.is_valid():
               jobfrm1.save()
          return redirect('jobpage')
          
     return render(request,'jobpage.html',{'jbup':jobfrm})


def test_dt(request):

     tst=test()

     if request.method=='POST':
          carname=request.POST.get('cars')
          lan=request.POST.get('fav_language')
          tst=test.objects.create(carname=carname,gender=lan)
          tst.save()

     return render(request,'test.html')





     
# Create your views here.
