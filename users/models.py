from django.db import models
from django import forms
from django.contrib.auth.models import User

GENDER_CHOICES =[
    ("1", "Мужской "),
    ("2", "Женский"),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    img = models.ImageField(default = 'default.jpg', upload_to = 'user_images')
    check_agree = models.BooleanField(default = True, verbose_name = "Согланешие об отправке уведомлений на электронную почту")
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES)

    def __str__(self):
        return f'Профаил пользователя {self.user.username}'
