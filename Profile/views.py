from Car_Rental.models import Car_Reservation
from Countries.models import Experience, Comments
from hotel.models import HotelReservationRequest
from .forms import registerForm, EditProfileForm
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, update_session_auth_hash

from django.contrib.auth.decorators import login_required



def addUser(request):
    form = registerForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
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
    if user.blk_flg == True:

        return render(request, 'BlkMsg.html')

    hotels = HotelReservationRequest.objects.filter(user_id=user.id)
    cars = Car_Reservation.objects.filter(user_id=user.id)
    posts = Experience.objects.filter(user_ID=user.id)
    comments = Comments.objects.filter(user_ID=user.id)

    args = {'user': user , 'hotels': hotels , 'cars': cars , 'posts': posts , 'comments': comments}

    return render(request, 'myAccount.html', args)



def editAccount(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('Profile/profile/')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
    return render(request, 'EditProfile.html', args)



def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('Profile/profile/')
        else:
            return redirect('Profile/editpassword/')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
    return render(request, 'ChangePassword.html', args)











































