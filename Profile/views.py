from .forms import SignUpForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate,login

# Create your views here.

def addUser(request):
	form = SignUpForm(request.POST or None)
	if form.is_valid():
		form.save()
		username = form.cleaned_data.get('username')
		userpassword = form.cleaned_data.get('password1')
		user = authenticate(username = username , password = userpassword )
		# if user:
		# 	login(request,user)
		# 	return redirect('/Profile/')   # Redirect to a Profile page.
		# else:
		# 	return render(request, 'SignUp.html', {'form': form})
	return render(request, 'SignUp.html', {'form':form})

