from .forms import SignUpForm,LogInForm
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate,login
from .models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
# Create your views here.

def temphome(request):
        allUsers = User.objects.all()
        context = {'allUsers' : allUsers}
        return render(request,'temphome.html',context)

def addUser(request):
        form = SignUpForm()
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                #return HttpResponseRedirect('/Profile/home/myprofile')   Go To UserProfile
        return render(request, 'SignUp.html', {'form':form})

def loginUser(request):
        form = LogInForm()
        if request.method == "POST":
            form = LogInForm(request.POST)
            username = request.POST['username']
            password = request.POST['user_password']
            try:
                user = User.objects.get( username = username , user_password = password)
                blk_flg_object = User._meta.get_field('blk_flg')
                blk_flg_value = blk_flg_object.value_from_object(user)
                user_id_object = User._meta.get_field('user_id')  #....7a7tago f al history
                user_id_value = user_id_object.value_from_object(user)
                if not blk_flg_value:
                    return render(request, 'myProfile.html', {'user': user})
                elif blk_flg_value:
                    return render(request, 'BlkMsg.html', {'user': user})
            except  User.DoesNotExist:
                messages.error(request, 'Invalid Username or Password .......')
                return render(request, 'LogIn.html', {'form': form})

        return render(request, 'LogIn.html', {'form':form})



# def handler404(request):
#         response = render_to_response('404.html', {},
#                                   context_instance=RequestContext(request))
#         response.status_code = 404
#         return response

