from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UseerOurRegistration

def register(request):
    if request.method == "POST":
            form = UseerOurRegistration(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Пользователь {username} был успешно создан')
                return redirect('main-home')

    else:
        form = UserCreationForm()

    return render(request, 'users/registration.html', {'form':form, 'title': 'Регистрация пользователя'})
