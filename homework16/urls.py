
from django.contrib import admin
from django.urls import include, path
from users import views as userViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', userViews.register, name = 'reg'),
    path('', include('main.urls')),
]
