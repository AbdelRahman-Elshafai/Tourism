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
			#return HttpResponseRedirect('')  ........... You should direct the user to his profile here after registeration
	return render(request, 'SignUp.html', {'form':form})

