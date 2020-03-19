
from django.contrib import admin
from django.urls import include, path
from users import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', userViews.register, name = 'reg'),
    path('user/', authViews.LoginView.as_view(template_name = 'users/user.html') , name = 'user'),
    path('exit/', authViews.LoginView.as_view(template_name = 'users/exit.html') , name = 'exit'),
    path('', include('main.urls')),
]
