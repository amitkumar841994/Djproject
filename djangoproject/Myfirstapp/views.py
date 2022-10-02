from cgitb import html
import re
from unicodedata import name
from django.shortcuts import redirect, render,HttpResponse
from .models import Food
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
# Create your views here.
