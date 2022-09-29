import re
from unicodedata import name
from django.shortcuts import render,HttpResponse
def index(request):
     return render(request,'index.html')
def food(request):
     id=request.POST.get('FoodID')
     name=request.POST.get('Foodname')
     price=request.POST.get('Foodprice')
     cate=request.POST.get('Foodcat')
     food=[{'f1':id,'f2':name,'f3':price,'f4':cate}]
     return render(request,'Food.html',{'f1':id,'f2':name,'f3':price,'f4':cate})
# Create your views here.
