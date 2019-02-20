from .forms import registerForm
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate



def addUser(request):
    form = registerForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/Tourism/home')
        else:
            return render(request, 'SignUp.html', {'form': form})

    return render(request, 'SignUp.html', {'form': form})

# Create your views here.

# def signupUser(request):
#     form = SignUpForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         username = form.cleaned_data.get('username')
#         raw_password = form.cleaned_data.get('password')
#         user = authenticate(request=request , username=username , password=raw_password)
#         if user is not None:
#             login(request , user)
#             return redirect('/Tourism/home')
#         else:
#             return render(request, 'SignUp.html', {'form': form})
#
#     return render(request, 'SignUp.html', {'form':form})







def viewAccount(request):
    user = request.user
    context = {'user': user }
    return render(request, 'myAccount.html', context)











































