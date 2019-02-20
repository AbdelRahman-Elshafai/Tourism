from .forms import SignUpForm
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate,login
from .models import UserProfile
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import login

# Create your views here.

def signupUser(request):
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate( username = username , password = password )
            login(request,user)
            return redirect('/Tourism/home')            #..................go to user profile
    else:
        form = SignUpForm()

    return render(request, 'SignUp.html', {'form':form})


def viewAccount(request):
    user = request.user
    context = {'user': user }
    return render(request, 'myAccount.html', context)




