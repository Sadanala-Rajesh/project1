from django import forms 
from .models import *
  
class PostForm(forms.ModelForm): 
  
    class Meta: 
        model = Post 
        fields = ['user','title','text','image']

class LoginForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=30,widget=forms.PasswordInput)
