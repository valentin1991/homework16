from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.db import models
from django.db.models import Model


class UseerOurRegistration(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ProfileImage, self).__init__(*args, **kwards)
        self.fields['img'].label = "Изображение профиля"

    class Meta:
        model = Profile
        fields = ['img']

class EmaiDeliveryAgree(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['check_agree']


class GenderSelection(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender']
