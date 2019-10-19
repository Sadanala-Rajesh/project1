from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
#from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect 
from .forms import *

def home(request):
	"1111111111111111111111111111111111111111111111111111111"
	if request.session.has_key('username'):
		name = request.session['username']
	else:
		name = None
	data = Post.objects.all()
	return render(request,'readmore.html',{'data':data})
	#return render(request,'nn.html')

def signup_post(request):
	if request.method =="POST":
		form =UserCreationForm(request.POST)
		if form.is_valid():
			username1 = request.POST.get('username')
			password1 = request.POST.get('password')
			user = User.objects.create_user(username=username1,password=password1)
			user.save()
			return HttpResponseRedirect('/')
	else:
		form = UserCreationForm()
	return render(request,'signup.html',{'form':form})

def login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form .is_valid():
			username1 = request.POST.get('username')
			password1 = request.POST.get('password')
			user = User.objects.filter(username=username1,password=password1)
			#if user:
			#	login(request,user)
			request.session['username'] = username1
			#name = request.session['username']
			if user != None:
				user = User.objects.get(username=username1)
				idd = user.username
				return HttpResponseRedirect('/individual_post/'+str(idd))
			else:
				return HttpResponse('Enter valid username and password')
	else:
		form = LoginForm()
	return render(request,'login.html',{'form':form})
def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return HttpResponseRedirect('/')
		
@login_required(login_url='/login/')  
def Post_view(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			name = request.session['username']
			return HttpResponseRedirect("/individual_post/"+str(name))
	else:
		form = PostForm()
	return render(request, 'post_form.html', {'form' : form})

def individual_post_data(request, name):
	if request.session.has_key('username'):
		if request.method == 'GET':
			user = User.objects.get(username = name)
			data = Post.objects.filter(user=user)
			name = request.session['username']
		return render(request,'individual.html',{'data':data,'name':name})
	else:
		return HttpResponseRedirect('/login/')

def delete_post(request,id):
	instance = Post.objects.get(id = id)
	instance.delete()
	name = request.session['username']
	return HttpResponseRedirect('/individual_post/'+str(name))

  


# name = request.session['username']
        	# title = request.POST.get('title')
        	# text = request.POST.get('text')
        	# image = request.POST.get('image')
        	# print(title,text,image)