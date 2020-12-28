from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, UpdateForm
from .models import ProfileImage

from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful')
            return redirect(request.path)
        else:
            messages.error(request, 'Registration Failed, Try Again')
            return render(request, 'accounts/register.html', {'form':form})
    else:
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            messages.success(request, 'login successful')
            return redirect('home')
        else:
            messages.error(request, 'login failed')
            return render(request, 'accounts/login.html', {'err': True})
    else:
        return render(request, 'accounts/login.html')

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'accounts/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def edit_profile(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.info(request, 'profile updated')
            return redirect(request.path)
        else:
            return render(request, 'accounts/edit_profile.html', {'form':form})
    else:
        form = UpdateForm(instance = request.user)
        return render(request, 'accounts/edit_profile.html', {'form':form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(request.path)
        else:
            return render(request, 'accounts/edit_profile.html', {'form':form})
    else:
        form = PasswordChangeForm(user = request.user)
        return render(request, 'accounts/edit_profile.html', {'form':form})


@login_required(login_url='/accounts/login/')
def upload_photo(request):
    if request.method == 'POST':
        photo = request.FILES['photo']
        user = request.user
        if user.profileimage:
            user.profileimage.image = photo
            user.profileimage.save()
        else:
            obj = ProfileImage(image = photo, user = user)
            obj.save()
        return redirect('home')

    return render(request, 'accounts/upload_photo.html')