from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    img = models.ImageField(default = 'default.jpeg', upload_to = 'user_images')

    def __str__(self):
        return f'Профаил пользователя {self.user.username}'
