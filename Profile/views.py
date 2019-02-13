from .forms import RegisterationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

def addUser(request):
	form = RegisterationForm()
	if request.method == "POST":
		form = RegisterationForm(request.POST)
		if form.is_valid():
			form.save()
			##return HttpResponseRedirect('Profile/home') Redirect to the Home Page
	return render(request, 'SignUp.html', {'form':form})

