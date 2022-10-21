from cgitb import html
from itertools import product
from math import prod
import re

from unicodedata import name
from django.shortcuts import redirect, render,HttpResponse
import requests
from .models import Food,User,Store
from .forms import Foodform, UserForm
def index(request):
     return render(request,'index.html')
def food(request):
     if request.method=='POST':
          food_data=Food()
          food_data.Food_id=request.POST.get('FoodID')
          food_data.Food_name=request.POST.get('Foodname')
          food_data.Food_price=request.POST.get('Foodprice')
          food_data.Food_cate=request.POST.get('Foodcat')
          food_data.save()
          return redirect('food')
     else:
          food_data=Food.objects.all()
          return render(request,'Food.html',{'food_dt':food_data})

def login(request):
     return render(request,'Login.html')     

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

def store_api(request):
     data=requests.get('https://fakestoreapi.com/products/')
     apidata=data.json()
     product=Store()
     # for i in range(len(apidata)):
     #      print(i)
     #      product=Store()
     #      product.title=apidata[i]['title']
     #      product.descriptions=apidata[1]['description']
     #      product.img=apidata[i]['image']
     #      product.price=apidata[i]['price']
     #      product.category=apidata[i]['category']
     #      product.save()
     
     return render(request,'productdata.html',{'str_data':apidata})

def viewstore(request,pid):
     viewdata=Store.objects.get(id==pid)
     print(viewdata)

     return render(request,'Viewstore.html',{'dt':viewdata})


# Create your views here.
