from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UseerOurRegistration(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
