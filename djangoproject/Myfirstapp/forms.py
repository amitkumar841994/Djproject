from dataclasses import fields
from pyexpat import model
from statistics import mode
from django import forms
from .models import Food,User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class Foodform(forms.ModelForm):
    class Meta:
        model=Food
        fields = '__all__'