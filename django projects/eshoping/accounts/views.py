from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import RegistrationForm, EditForm
from .models import ProfilePicture, UserAccounts

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from django.contrib import messages

# Create your views here.

# def register(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     if request.method == "POST":   
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(request.path)
#         else:
#             return render(request, 'accounts/register.html', {'form' : form})

#     else:
#         form = RegistrationForm()
#         return render(request, 'accounts/register.html', {'form' : form})

class RegisterView(View):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
        else:
            return render(request, self.template_name, {'form' : form})

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})


def login_process(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {"error": True})

    return render(request, 'accounts/login.html')

# @login_required
# def home(request):
#     return render(request, 'accounts/index.html')

class HomeView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = 'accounts/index.html'
    model = UserAccounts

def logout_process(request):
    logout(request)
    return redirect('login')


@login_required
def edit_profile(request):
    if request.method == "POST":   
        form = EditForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect(request.path)
        else:
            return render(request, 'accounts/edit_profile.html', {'form' : form})

    else:
        form = EditForm(instance = request.user)
        return render(request, 'accounts/edit_profile.html', {'form' : form})


@login_required
def upload_photo(request):
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        profile_data = request.user.profilepicture
        if profile_data:
            profile_data.image = photo
            profile_data.save()
        else:
            obj = ProfilePicture(user = request.user, image = photo)
            obj.save()
        return redirect('edit')



@login_required
def edit_password(request):
    if request.method == "POST":   
        form = PasswordChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(request.path)
        else:
            return render(request, 'accounts/edit_profile.html', {'form' : form})

    else:
        form = PasswordChangeForm(user = request.user)
        return render(request, 'accounts/edit_profile.html', {'form' : form})


def check_user_exists(request, username):
    if UserAccounts.objects.filter(username = username).exists():
        return HttpResponse('error')
    else:
        return HttpResponse('valid')
    