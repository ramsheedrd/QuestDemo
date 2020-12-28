from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserAccounts
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserAccounts
        fields = ["username", "first_name", "last_name", "email", "phone", "dob"]
        widgets = {"dob": forms.DateInput(attrs={'type':'date'})}

class EditForm(UserChangeForm):
    class Meta:
        model = UserAccounts
        fields = ["username", "first_name", "last_name", "email", 'phone', 'dob']
        widgets = {"dob": forms.DateInput(attrs={'type':'date'})}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields["password"]
    